"""Dependency-parsing evaluation helpers.

The notebook contains the full experiment pipeline. This small module extracts
one reusable piece of logic so the repository has a testable code path outside
Jupyter: unlabeled and labeled attachment score calculation on aligned head and
label sequences.
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence

IGNORE_INDEX = -1


def attachment_scores(
    gold_heads: Sequence[int],
    predicted_heads: Sequence[int],
    gold_labels: Sequence[str],
    predicted_labels: Sequence[str],
    *,
    ignore_indices: Iterable[int] | None = None,
) -> dict[str, float | int]:
    """Return UAS/LAS for one aligned sentence.

    Positions listed in ``ignore_indices`` are skipped. This is useful for the
    synthetic ROOT position and for padding positions in batched evaluation.
    """
    lengths = {len(gold_heads), len(predicted_heads), len(gold_labels), len(predicted_labels)}
    if len(lengths) != 1:
        raise ValueError("gold and predicted heads/labels must have the same length")

    ignored = set(ignore_indices or [])
    total = 0
    head_correct = 0
    label_correct = 0

    for index, (gold_head, pred_head, gold_label, pred_label) in enumerate(
        zip(gold_heads, predicted_heads, gold_labels, predicted_labels)
    ):
        if index in ignored or gold_head == IGNORE_INDEX:
            continue

        total += 1
        if gold_head == pred_head:
            head_correct += 1
            if gold_label == pred_label:
                label_correct += 1

    if total == 0:
        return {"UAS": 0.0, "LAS": 0.0, "token_count": 0}

    return {
        "UAS": head_correct / total,
        "LAS": label_correct / total,
        "token_count": total,
    }
