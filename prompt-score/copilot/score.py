import re,sys,json
# Python port of hooks/score.ts (same rules as codex/score.mjs). Embedded in the Copilot agent's instructions.
def h(t,p,f=re.I|re.A):return re.search(p,t,f) is not None
def score(text):
 t=text.strip();w=len(t.split());c=[]
 def a(n,m,g,tip):c.append({'name':n,'max':m,'got':max(0,min(m,round(g))),'tip':tip})
 a('Clear goal',15,(10 if h(t,r"\b(create|build|write|fix|add|implement|refactor|review|analy[sz]e|compare|design|explain|generate|plan|debug|summari[sz]e|convert|find)\b") or h(t,'(צור|כתוב|תקן|הוסף|בנה|נתח|השווה|תכנן|הסבר|סכם|מצא)') else 3)+(5 if w>=8 else 2 if w>=4 else 0),'Open with one concrete action verb and the single outcome you want.')
 a('Context',15,(8 if h(t,r"\b(because|currently|so that|background|context|we are|i am|project|existing|goal is)\b") or h(t,'(כי|כרגע|הקשר|פרויקט|מטרה)') else 0)+(7 if h(t,r"[\w./\\-]+\.\w{1,5}\b|`[^`]+`|https?://") else 0),'Say why, what exists today, and point at files, links or code.')
 a('Constraints',15,15 if h(t,r"\b(must|should|only|don't|do not|never|avoid|without|at most|at least|limit|max|min)\b") or h(t,'(חייב|רק|אסור|בלי|הימנע|מקסימום|מינימום)') else 0,'State must / must-not rules: scope, tech, style, limits.')
 a('Output format',15,15 if h(t,r"\b(format|table|list|bullet|json|markdown|yaml|csv|steps|sections?|summary|diff|code block|in hebrew|in english)\b") or h(t,'(טבלה|רשימה|בעברית|באנגלית|פורמט|סעיפים)') else 0,'Say what the answer should look like: format, language, length.')
 a('Success criteria / examples',15,15 if h(t,r"\b(test|verify|done when|acceptance|criteria|example|e\.g\.|for instance|expected|success)\b") or h(t,'(בדיקה|אימות|קריטריון|לדוגמה|צפוי)') else 0,'Define "done" or give an example of good output.')
 a('Specifics',10,(4 if h(t,r"\d") else 0)+(3 if h(t,r"[A-Z][a-z]+[A-Z]|_\w+|\(\)|\bv?\d+\.\d+",re.A) else 0)+(3 if h(t,r"\"[^\"]+\"|'[^']+'") else 0),'Use names, numbers, versions and quoted literals instead of vague words.')
 a('Structure',10,(6 if h(t,r"\n\s*([-*]|\d+[.)])\s") else 0)+(2 if '\n' in t else 0)+(2 if h(t,r"^#|\n#|:\s*\n|<\w+>") else 0),'Break it up: bullets, numbered steps, or labelled sections.')
 a('Length fit',5,0 if w<4 else 2 if w<12 else 5 if w<=400 else 3,'Too terse: add detail.' if w<12 else 'Trim anything that is not needed.')
 s=max(1,min(100,sum(x['got'] for x in c)));lab='excellent' if s>=80 else 'good' if s>=60 else 'fair' if s>=40 else 'weak'
 g=sorted(c,key=lambda x:x['got']-x['max'])[0]
 return {'score':s,'label':lab,'checks':c,'line':f"Prompt score: {s}/100 ({lab}) - biggest gap: {g['name']}. {g['tip']}"}
if __name__=='__main__':
 a=[x for x in sys.argv[1:] if x!='--json'];r=score(' '.join(a) if a else sys.stdin.read())
 print(json.dumps(r,ensure_ascii=False,indent=2) if '--json' in sys.argv else r['line'])
