"""
compare.py

Utilities for comparing detection results across techniques and
producing summary statistics.
"""

from collections import defaultdict
import csv


def compute_rates(rows) -> dict:
    """
    rows: list of dicts with keys 'technique' and 'detected' (0/1).
    Returns: dict of {technique: {'total', 'detected', 'detection_rate'}}.
    """
    counts = defaultdict(lambda: {"total": 0, "detected": 0})
    for row in rows:
        counts[row["technique"]]["total"] += 1
        counts[row["technique"]]["detected"] += int(row["detected"])

    rates = {}
    for technique, c in counts.items():
        total = c["total"]
        rates[technique] = {
            "total": total,
            "detected": c["detected"],
            "detection_rate": c["detected"] / total if total else 0.0,
        }
    return rates


def summarise(rates: dict, order=None) -> str:
    """Return a human-readable summary string."""
    keys = order or list(rates.keys())
    lines = []
    for k in keys:
        if k not in rates:
            continue
        r = rates[k]
        pct = r["detection_rate"] * 100
        lines.append(f"{k:15s}  {r['detected']:3d}/{r['total']:3d}  ({pct:5.1f}%)")
    return "\n".join(lines)


def write_csv(rates: dict, path: str, order=None) -> None:
    """Write detection rates to a CSV file."""
    keys = order or list(rates.keys())
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["technique", "total", "detected", "detection_rate"])
        for k in keys:
            if k not in rates:
                continue
            r = rates[k]
            writer.writerow([k, r["total"], r["detected"],
                             f"{r['detection_rate']:.3f}"])


def drop_in_detection(original_rate: float, technique_rate: float) -> float:
    """Return the absolute drop in detection rate."""
    return original_rate - technique_rate
