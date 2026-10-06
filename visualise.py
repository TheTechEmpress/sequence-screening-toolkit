"""
visualise.py

Plotting utilities for detection rate results.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_detection_rates(rates: dict, path: str, order=None,
                         title: str = "Detection rate by technique") -> None:
    """Save a bar chart of detection rates to the given path."""
    keys = order or list(rates.keys())
    keys = [k for k in keys if k in rates]
    values = [rates[k]["detection_rate"] * 100 for k in keys]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(keys, values, color="#2E86AB")
    plt.ylabel("Detection rate (%)")
    plt.title(title)
    plt.ylim(0, 105)
    for bar, v in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, v + 2,
                 f"{v:.0f}%", ha="center", va="bottom", fontsize=10)
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()
