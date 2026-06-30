# Reproduction Notes

This file records the current public-reproduction target for the notebook.

## Intended environment

- Python dependencies: see `requirements.txt`
- Random seed used in the notebook: `42`
- Original interactive runtime: Google Colab with a T4 GPU
- Data snapshot: Universal Dependencies release tag `r2.18`

## Expected notebook checks

A lightweight rerun should confirm these early cells before training:

- The seed cell prints `Seed: 42`.
- The data-download cell prepares `UD_Czech-PDT` and `UD_English-EWT`.
- The subset-loading cell reports 2,000 train / 500 dev / 500 test sentences for each language.

## Reported held-out results

The README table reports punctuation-excluded held-out UAS/LAS from the saved notebook run.
Small numerical differences may occur across PyTorch, CUDA, and hardware versions.

## Current limitation

The full notebook training run is still the source of truth for the reported numbers. The repository now includes a small tested metrics helper, but the full parser has not yet been refactored into a package.
