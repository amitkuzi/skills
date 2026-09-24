# Slant 3D research coverage

- **Catalog cutoff:** 2026-09-24
- **Channel surface:** public long-form uploads visible on the official Slant 3D YouTube `Videos`
  tab. Shorts, Live, unavailable/private items, and material outside that tab were not part of the
  requested corpus.
- **Cataloged and screened:** 635 unique videos across 22 exhausted catalog pages.
- **Screening result:** 185 definite relevance, 49 probable relevance, and 401 excluded after
  first-party metadata screening.
- **Full-caption deep review:** all 185 definite videos and all 49 probable videos.
- **Probable reclassification:** 34 included and 15 excluded after complete-caption review.
- **Videos contributing to the knowledge base:** 219 (185 definite + 34 promoted probable).
- **Timestamped claim records:** 970 (890 in definite batches 01-08 + 80 in promoted probable
  videos), each with conditions/exceptions and a confidence label.
- **Automated coverage check:** the eight definite batches contain all 185 definite IDs exactly once;
  the probable manifest contains all 49 probable IDs exactly once; the three screening sets are
  disjoint and total 635.

## Evidence method

The catalog and screening used official channel metadata, descriptions, displayed chapters, and
transcript availability. Deep review used each selected video's complete official original-English
automatic-caption track (`en-orig`) plus official metadata. Claims are paraphrased and link to the
official video timestamp; full transcripts were not retained.

Confidence describes whether the written claim accurately represents the accessible spoken evidence,
not whether the engineering claim is true. Independent technical validation is recorded separately in
`independent-validation-2026-09-24.md`.

## Important limitation

The deep review did not perform frame-by-frame visual interpretation of every video. Dimensions,
diagrams, CAD operations, or geometry shown only on screen and not explained in the captions were not
inferred. This avoids inventing visual details, but it means a future visual audit may add evidence.
Automatic captions can also contain transcription errors; ambiguous numbers and units were excluded
from portable rules.

## Main evidence files

- Complete catalog: `slant3d-youtube-long-form-catalog-2026-09-24.md`
- Screening: `relevant-video-candidates-2026-09-24.md`
- Definite claims: `claims/core-design-orientation-batch-01.md` through
  `claims/core-design-orientation-batch-08.md`
- Probable review: `claims/probable-video-deep-review.md`
- Independent validation: `independent-validation-2026-09-24.md`
- Automated coverage tests: `../tests/test_research_coverage.py`
