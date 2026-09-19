from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


HERE = Path(__file__).resolve().parent
DATA_PATH = HERE / "data" / "bubble_dynamics_metrics.csv"
OUTPUT_PATH = HERE / "summary" / "sun2017_departure_period.png"


def main() -> None:
    data = pd.read_csv(DATA_PATH)

    points = data[data["metric"] == "departure_period"].copy()
    points = points.sort_values("series_number")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        points["series_number"],
        points["value"],
        marker="o",
        linestyle="None",
    )

    ax.set_xlabel("Bubble series number")
    ax.set_ylabel("Bubble departure period (ms)")
    ax.set_title("Sun et al. (2017): Bubble departure period")
    ax.grid(True, alpha=0.3)

    fig.savefig(OUTPUT_PATH, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved plot to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()