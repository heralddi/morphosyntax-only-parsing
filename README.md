# Morphosyntax-Only Parsing: Czech vs. English

How much dependency structure can be recovered from **morphosyntactic information alone** — and does the answer differ between a morphologically rich language (Czech) and an analytic one (English)?

This project isolates that question by training **the same graph-based dependency parser** under three input conditions and comparing them across two Universal Dependencies treebanks:

| Setting | Input |
|---|---|
| `lexicalized` | word identity only |
| `morphosyntax-only` | gold UPOS + gold UFeats only |
| `mixed` | both |

Gold tags are used deliberately, so the comparison reflects the available syntactic *signal*, not upstream tagging noise.

> Final project for **Computational Linguistics (Prof. Alexander Koller), Saarland University**, winter semester 2025/26 — awarded full marks.
> Author: **Bao (Herald) Di**

## Results (held-out test, punctuation excluded)

| Language | Representation | UAS | LAS |
|---|---|---|---|
| Czech | lexicalized | 0.2189 | 0.1318 |
| Czech | **morphosyntax-only** | **0.4382** | **0.4017** |
| Czech | mixed | 0.4212 | 0.3749 |
| English | lexicalized | 0.2542 | 0.1770 |
| English | morphosyntax-only | 0.3409 | 0.2871 |
| English | **mixed** | **0.3398** | **0.2949** |

**Main finding:** morphosyntactic information carries most of the recoverable syntactic signal, and far more so in Czech: the LAS gain of `morphosyntax-only` over `lexicalized` is **+0.27 in Czech vs. +0.11 in English**. In Czech, adding lexical identity on top of morphosyntax does not help — `mixed` does *not* overtake `morphosyntax-only`.

Additional analyses in the notebook/report:

- **Greedy vs. MST decoding** (Czech dev: UAS 0.4692 → 0.4768; a small but consistent gain for tree-constrained decoding)
- **Label-confusion analysis** (which dependency labels are confused under each setting)
- **Dependency-length breakdown** (morphosyntax-only holds up much better on long dependencies: LAS at distance 7+ in Czech 0.2278 vs. 0.0547 lexicalized)

## Method

A graph-based dependency parser implemented **from scratch in PyTorch**: embeddings for words / UPOS / morphological-feature bundles feed an explicit arc scorer over head–dependent pairs; training uses padded, masked mini-batches with a synthetic ROOT token; inference uses **maximum-spanning-tree (Chu–Liu/Edmonds) decoding** to enforce a legal tree. Only `conllu` (CoNLL-U reading) and `networkx` (MST routine) are used as utilities — the data pipeline, model, training loop, decoding, and evaluation are implemented directly.

## Data

Universal Dependencies treebanks **UD_Czech-PDT** and **UD_English-EWT**, subsampled to 2,000 train / 500 dev / 500 test sentences per language. Model selection on dev LAS only; the test set is used once.

## Files

- `final_project_morphosyntax_parsing_cz_en.ipynb` — full pipeline: data loading, encoding, model, training, decoding, evaluation, analyses
- `Final_Project.pdf` — project report

## Run it

The notebook runs end-to-end in a single Colab session (~5 minutes on a T4 GPU; the longest part is training the 3 × 2 parser settings).

Local environment: Python 3.14, PyTorch 2.10-dev, NumPy 2.3.3, `conllu` 6.0.0, `networkx` 3.5.
