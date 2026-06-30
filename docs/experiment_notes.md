# Experiment Notes

This project asks how much dependency structure can be recovered from morphosyntactic information alone, using Czech and English as a small contrast between a morphologically rich language and a more analytic one.

## Why gold morphology?

The experiments use gold UPOS and UFeats so that the comparison focuses on the syntactic signal available in morphosyntactic annotations. This deliberately avoids mixing the parser comparison with upstream tagging errors.

## What the comparison can show

The three representation settings separate different sources of information:

- `lexicalized`: word identity only
- `morphosyntax-only`: gold UPOS and UFeats only
- `mixed`: word identity plus morphosyntax

The key question is whether morphology alone carries enough information to recover useful dependency structure, and whether that contribution is stronger in Czech than in English.

## What the comparison cannot show

The setup does not make a state-of-the-art parsing claim. It uses small treebank subsets, a simple graph-based parser, and gold tags. The results are best read as a controlled probe of morphosyntactic cue strength rather than as a general benchmark for dependency parsing.

## Possible extensions

Natural follow-up experiments include adding simple baselines, testing another morphologically rich language, and separating individual feature families such as case, number, gender, and verb features.
