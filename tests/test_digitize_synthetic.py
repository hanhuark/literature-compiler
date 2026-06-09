from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from litcomp.digitize import AxisCalibration, detect_colored_points


def _make_synthetic_plot(path: Path) -> None:
    image = Image.new("RGB", (240, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.line((40, 160, 220, 160), fill="black", width=2)
    draw.line((40, 160, 40, 20), fill="black", width=2)
    for x, y in [(70, 130), (120, 95), (180, 55)]:
        draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill="red")
    image.save(path)


def test_detects_red_points_and_maps_to_data_coordinates(tmp_path: Path):
    image_path = tmp_path / "plot.png"
    _make_synthetic_plot(image_path)
    calibration = AxisCalibration(
        x_pixel_min=40,
        x_pixel_max=220,
        y_pixel_min=160,
        y_pixel_max=20,
        x_data_min=0,
        x_data_max=30,
        y_data_min=0,
        y_data_max=300_000,
    )

    points = detect_colored_points(image_path, calibration, target_rgb=(255, 0, 0), tolerance=80)

    assert len(points) == 3
    xs = np.array([point.x for point in points])
    ys = np.array([point.y for point in points])
    np.testing.assert_allclose(xs, [5.0, 13.333333, 23.333333], rtol=0.04, atol=0.2)
    assert ys[0] > 50_000
    assert ys[-1] > ys[0]
    assert all(0.0 <= point.confidence <= 1.0 for point in points)
