# Morphosyntax-Only Parsing: Czech vs. English

How much dependency structure can be recovered from **morphosyntactic information alone** — and does the answer differ between a morphologically rich language (Czech) and an analytic one (English)?

This project isolates that question by training **the same graph-based dependency parser** under three input conditions and comparing them across two Universal Dependencies treebanks:

| Setting | Input |
|---|---|
| `lexicalized` | word identity only |
| `morphosyntax-only` | gold UPOS + gold UFeats only |
| `mixed` | both |

Gold tags are used deliberately, so the comparison reflects the available syntactic *signal*, not upstream tagging noise. In the notebook code, the morphosyntax-only setting is named `morphosyntax_only`.

Course project for **Computational Linguistics (Prof. Alexander Koller), Saarland University**, winter semester 2025/26.
Author: **Bao (Herald) Di**

## Why this project

Morphological features can act as cues for syntactic structure, but languages differ in how much overt morphology they provide. A small controlled parser comparison is one way to ask how much syntactic information is recoverable from those cues before adding richer lexical or contextual information.

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

A graph-based dependency parser implemented directly in PyTorch: embeddings for words / UPOS / morphological-feature bundles feed an explicit arc scorer over head–dependent pairs; training uses padded, masked mini-batches with a synthetic ROOT token; inference uses **maximum-spanning-tree (Chu–Liu/Edmonds) decoding** to enforce a legal tree. The project uses `conllu` for CoNLL-U reading and `networkx` for the MST routine.

## Data

Universal Dependencies treebanks **UD_Czech-PDT** and **UD_English-EWT**, subsampled to 2,000 train / 500 dev / 500 test sentences per language. Model selection on dev LAS only; the test set is used once.

## Limitations

This is a small controlled course project rather than a state-of-the-art parser. The experiments use gold UPOS and UFeats to isolate morphosyntactic signal, and the treebanks are subsetted to keep the comparison lightweight. The parser architecture is intentionally simple, so the results should be read as controlled evidence about available morphosyntactic cues rather than as general parsing-performance claims.

## Files

- `final_project_morphosyntax_parsing_cz_en.ipynb` — full pipeline: data loading, encoding, model, training, decoding, evaluation, analyses
- `Final_Project.pdf` — project report

## Quick start

Install the Python dependencies, then run the notebook:

```bash
pip install -r requirements.txt
jupyter notebook final_project_morphosyntax_parsing_cz_en.ipynb
```

The notebook downloads the UD treebanks into a local `data/` directory when run. It was originally run in a Colab session on a T4 GPU; results may vary slightly across PyTorch/CUDA versions.

## Data attribution

The experiments use Universal Dependencies data from the official GitHub treebank repositories:

- [`UD_Czech-PDT`](https://github.com/UniversalDependencies/UD_Czech-PDT)
- [`UD_English-EWT`](https://github.com/UniversalDependencies/UD_English-EWT)

The treebank data is downloaded during notebook execution and is not included in this repository.
