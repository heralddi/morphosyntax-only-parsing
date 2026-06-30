# Data Version Notes

The notebook uses two Universal Dependencies treebanks:

- `UD_Czech-PDT`
- `UD_English-EWT`

For reproducibility, the notebook clones the `r2.18` release tag of both treebank repositories instead of the moving default branch.

## Why pin a release tag?

Universal Dependencies treebanks are actively maintained. Pinning a release tag keeps the subset sampling, label inventory, and reported UAS/LAS numbers tied to a specific data snapshot rather than whichever commit happens to be current when the notebook is rerun.

## Local data directory

The notebook downloads treebanks into `data/`, which is intentionally ignored by Git. The treebank files are not redistributed in this repository.
