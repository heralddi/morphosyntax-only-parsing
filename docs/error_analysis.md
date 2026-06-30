# Error Analysis Notes

The notebook includes two small post-hoc analyses: dependency-label confusion and accuracy by dependency length. These notes summarize what those analyses are meant to show.

## Label confusions

The most useful label-confusion patterns are not just mistakes; they indicate which dependency relations are hard to recover from the available input representation.

Examples to inspect in future runs:

- Czech lexicalized models often collapse several labels into frequent adjectival or nominal relations.
- Czech morphosyntax-only models should be checked for `obl` / `obj` / `obl:arg` confusions.
- English morphosyntax-only models should be checked for `obl`, `obj`, and `nsubj` confusions, where surface morphology gives weaker cues.

## Dependency length

Distance-bucket results ask whether morphosyntactic cues help only on local dependencies or also on longer attachments. The current notebook suggests that morphosyntax-only input helps beyond the shortest dependencies, especially for Czech.

## Next step

A useful follow-up PR would export the notebook's confusion-counting logic into a small script that reads saved prediction records and writes a compact table.
