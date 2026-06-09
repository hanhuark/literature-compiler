from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image
from skimage.measure import label, regionprops

from .calibration import AxisCalibration


@dataclass(frozen=True)
class DigitizedPoint:
    x: float
    y: float
    confidence: float
    pixel_x: float
    pixel_y: float


def detect_colored_points(
    image_path: str | Path,
    calibration: AxisCalibration,
    target_rgb: tuple[int, int, int],
    tolerance: float = 60.0,
) -> list[DigitizedPoint]:
    image = np.asarray(Image.open(image_path).convert("RGB"), dtype=float)
    target = np.asarray(target_rgb, dtype=float)
    distance = np.linalg.norm(image - target, axis=2)
    mask = distance <= tolerance
    regions = regionprops(label(mask))
    points: list[DigitizedPoint] = []
    for region in regions:
        if region.area < 5:
            continue
        y_pixel, x_pixel = region.centroid
        x_data, y_data = calibration.pixel_to_data(x_pixel, y_pixel)
        region_distance = distance[tuple(region.coords.T)].mean()
        confidence = max(0.0, min(1.0, 1.0 - float(region_distance / max(tolerance, 1.0))))
        points.append(DigitizedPoint(x_data, y_data, confidence, x_pixel, y_pixel))
    return sorted(points, key=lambda point: point.x)
