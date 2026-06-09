from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from .schema import DataPoint


def compile_points(points: Iterable[DataPoint]) -> pd.DataFrame:
    rows = [point.model_dump() for point in points]
    return pd.DataFrame(rows)


def save_points_csv(points: Iterable[DataPoint], path: str | Path) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    compile_points(points).to_csv(destination, index=False)
    return destination


def load_points_csv(path: str | Path) -> pd.DataFrame:
    return pd.read_csv(path)
