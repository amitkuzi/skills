<#
  Builds the Prompt Score agent for Microsoft Copilot (Windows).
    .\install.ps1            -> builds dist\prompt-score-copilot-<ver>.zip (Microsoft 365 Copilot agent package),
                                dist\consumer-prompt.txt (text-only setup prompt to paste into personal Copilot)
                                dist\custom-instructions.txt (permanent: paste into Copilot Settings > Personalization > Custom instructions)
                                and dist\PromptScore-Copilot-Setup-<ver>.zip (the one file
                                to hand a non-technical user: START HERE.html, the agent package, the PDF guide)
    .\install.ps1 -Consumer  -> also copies the permanent custom instructions to the clipboard and opens Copilot
    .\install.ps1 -NoOpen    -> build only, open nothing
  Version and release date come from ..\.claude-plugin\plugin.json (the one canonical source).
#>
param([switch]$Consumer, [switch]$NoOpen)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing

$here   = $PSScriptRoot
$dist   = Join-Path $here 'dist'
$stage  = Join-Path $dist 'appPackage'
$utf8   = New-Object System.Text.UTF8Encoding $false
$maxInstructions = 8000   # declarative agent manifest v1.5 limit
$maxCustom = 1500         # Copilot custom instructions: limit unpublished, 1,500 is the lowest reported figure

function Read-Text($path) { [IO.File]::ReadAllText($path, $utf8) }
function Write-Text($path, $text) { [IO.File]::WriteAllText($path, $text, $utf8) }
function Fail($what, $why, $next) { throw "$what failed: $why. Next step: $next" }

function Get-Release {
  $plugin = Read-Text (Join-Path $here '..\.claude-plugin\plugin.json') | ConvertFrom-Json
  if (-not $plugin.version -or -not $plugin.releaseDate) {
    Fail 'Reading the version' 'plugin.json has no version or releaseDate' 'add both to prompt-score\.claude-plugin\plugin.json'
  }
  @{ Version = $plugin.version; Date = $plugin.releaseDate }
}

function Get-EmbeddedScorer {
  # score.py without its comment header and command-line entry point
  $lines = (Read-Text (Join-Path $here 'score.py')) -split "`r?`n"
  $end = [Array]::FindIndex($lines, [Predicate[string]]{ param($l) $l.StartsWith('if __name__') })
  ($lines[0..($end - 1)] | Where-Object { -not $_.StartsWith('#') }) -join "`n"
}

function Expand-Template($text, $release) {
  $text.Replace('{{VERSION}}', $release.Version).Replace('{{DATE}}', $release.Date)
}

function New-Instructions($release) {
  $template = Read-Text (Join-Path $here 'instructions.template.md')
  $text = (Expand-Template $template $release).Replace('{{SCORER}}', (Get-EmbeddedScorer)).Trim()
  if ($text.Length -gt $maxInstructions) {
    Fail 'Building the instructions' "they are $($text.Length) characters, the Copilot limit is $maxInstructions" 'shorten instructions.template.md'
  }
  $text
}

function New-Icon($path, $size, [switch]$Outline) {
  $bmp = New-Object System.Drawing.Bitmap $size, $size
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.SmoothingMode = 'AntiAlias'
  $g.Clear([System.Drawing.Color]::Transparent)
  if (-not $Outline) { $g.Clear([System.Drawing.ColorTranslator]::FromHtml('#E4632D')) }
  $pad = [int]($size * 0.18); $box = $size - 2 * $pad
  $pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::White), ([Math]::Max(2, $size * 0.09))
  $pen.StartCap = 'Round'; $pen.EndCap = 'Round'
  $g.DrawArc($pen, $pad, $pad, $box, $box, 135, 270)                   # score gauge
  $c = $size / 2; $r = $box * 0.32
  $g.DrawLine($pen, $c, $c, $c + $r * [Math]::Cos(-0.6), $c + $r * [Math]::Sin(-0.6))   # needle near the top score
  $g.Dispose(); $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png); $bmp.Dispose()
}

function New-CustomInstructions($release) {
  # Short version for Copilot Settings > Personalization > Custom instructions: applies to every new chat
  $text = (Expand-Template (Read-Text (Join-Path $here 'custom-instructions.template.md')) $release).Trim()
  if ($text.Length -gt $maxCustom) {
    Fail 'Building the custom instructions' "they are $($text.Length) characters, the safe limit is $maxCustom" 'shorten custom-instructions.template.md'
  }
  $text
}

function New-ConsumerPrompt($release) {
  # Text-only setup prompt for personal Copilot: the same rules in plain words, no code
  (Expand-Template (Read-Text (Join-Path $here 'install-prompt.template.md')) $release).Trim()
}

function Build-AgentPackage($release, $instructions) {
  Remove-Item $stage -Recurse -Force -ErrorAction SilentlyContinue
  New-Item -ItemType Directory -Force $stage | Out-Null
  $escaped = (ConvertTo-Json $instructions).Trim('"')
  foreach ($name in 'manifest.json', 'declarativeAgent.json') {
    $text = (Expand-Template (Read-Text (Join-Path $here "appPackage\$name")) $release).Replace('{{INSTRUCTIONS}}', $escaped)
    try { $null = $text | ConvertFrom-Json } catch { Fail "Building $name" 'the result is not valid JSON' 'check the template for a stray quote or comma' }
    Write-Text (Join-Path $stage $name) $text
  }
  New-Icon (Join-Path $stage 'color.png') 192
  New-Icon (Join-Path $stage 'outline.png') 32 -Outline
  $zip = Join-Path $dist "prompt-score-copilot-$($release.Version).zip"
  Remove-Item $zip -Force -ErrorAction SilentlyContinue
  Compress-Archive -Path (Join-Path $stage '*') -DestinationPath $zip
  $zip
}

function Build-EasySetup($release, $agentZip, $consumerPrompt, $customInstructions, $instructions) {
  # One zip for non-technical users: a start page with copy buttons, the agent package and the PDF guide
  $folderName = 'Prompt Score for Copilot'
  $root = Join-Path $dist 'setup'
  $folder = Join-Path $root $folderName
  $agentName = 'PromptScore-Microsoft365-Copilot.zip'
  Remove-Item $root -Recurse -Force -ErrorAction SilentlyContinue
  New-Item -ItemType Directory -Force $folder | Out-Null
  Copy-Item $agentZip (Join-Path $folder $agentName)
  $manual = Join-Path $here 'docs\install-manual.pdf'
  if (-not (Test-Path $manual)) { Fail 'Building the setup zip' 'docs\install-manual.pdf is missing' 'run: node copilot\docs\build-manual.mjs' }
  Copy-Item $manual (Join-Path $folder 'Install guide.pdf')
  $page = Expand-Template (Read-Text (Join-Path $here 'docs\start-here.src.html')) $release
  $page = $page.Replace('{{AGENTZIP}}', $agentName).Replace('{{PROMPT}}', [Net.WebUtility]::HtmlEncode($consumerPrompt)).Replace('{{CUSTOM}}', [Net.WebUtility]::HtmlEncode($customInstructions)).Replace('{{AGENT}}', [Net.WebUtility]::HtmlEncode($instructions))
  Write-Text (Join-Path $folder 'Copilot at work - agent instructions.txt') $instructions
  Write-Text (Join-Path $folder 'Copilot permanent setup (Custom instructions).txt') $customInstructions
  Write-Text (Join-Path $folder 'Copilot setup text.txt') $consumerPrompt
  Write-Text (Join-Path $folder 'START HERE.html') $page
  $setupZip = Join-Path $dist "PromptScore-Copilot-Setup-$($release.Version).zip"
  Remove-Item $setupZip -Force -ErrorAction SilentlyContinue
  Add-Type -AssemblyName System.IO.Compression.FileSystem
  [IO.Compression.ZipFile]::CreateFromDirectory($folder, $setupZip, 'Optimal', $true)
  $setupZip
}

function Show-UploadSteps($zip) {
  Write-Host ''
  Write-Host "Agent package: $zip" -ForegroundColor Green
  Write-Host 'Upload it: Teams > Apps > Manage your apps > Upload an app > Upload a custom app > pick the zip > Add.'
  Write-Host 'Then open the Microsoft 365 Copilot app > Agents > Prompt Score.'
  Write-Host 'No "Upload a custom app" option? Your admin has to allow custom app upload, or upload it in Microsoft 365 admin center > Integrated apps.'
}

function Start-ConsumerCopilot($promptFile) {
  Set-Clipboard -Value (Read-Text $promptFile)
  Write-Host 'Custom instructions copied. In Copilot: Settings > Personalization > Custom instructions > paste > Save, then open a new chat.' -ForegroundColor Green
  Start-Process 'https://copilot.microsoft.com/'
}

# --- main story ---
$release = Get-Release
$instructions = New-Instructions $release
$zip = Build-AgentPackage $release $instructions
$promptFile = Join-Path $dist 'consumer-prompt.txt'
$consumerPrompt = New-ConsumerPrompt $release
Write-Text $promptFile $consumerPrompt
$customInstructions = New-CustomInstructions $release
Write-Text (Join-Path $dist 'custom-instructions.txt') $customInstructions
$setupZip = Build-EasySetup $release $zip $consumerPrompt $customInstructions $instructions
Write-Text (Join-Path $dist 'agent-instructions.txt') $instructions
Write-Host "Prompt Score v$($release.Version) ($($release.Date)) - agent instructions $($instructions.Length)/$maxInstructions chars, setup prompt $($consumerPrompt.Length) chars, custom instructions $($customInstructions.Length)/$maxCustom chars"
Write-Host "Setup for non-technical users (send this one file): $setupZip" -ForegroundColor Green
Show-UploadSteps $zip
if ($Consumer) { Start-ConsumerCopilot (Join-Path $dist 'custom-instructions.txt') }
if (-not $NoOpen) { Invoke-Item $dist }
