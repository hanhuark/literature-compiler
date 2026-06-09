from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AxisCalibration:
    x_pixel_min: float
    x_pixel_max: float
    y_pixel_min: float
    y_pixel_max: float
    x_data_min: float
    x_data_max: float
    y_data_min: float
    y_data_max: float

    def pixel_to_data(self, x_pixel: float, y_pixel: float) -> tuple[float, float]:
        x_fraction = (x_pixel - self.x_pixel_min) / (self.x_pixel_max - self.x_pixel_min)
        y_fraction = (y_pixel - self.y_pixel_min) / (self.y_pixel_max - self.y_pixel_min)
        x_data = self.x_data_min + x_fraction * (self.x_data_max - self.x_data_min)
        y_data = self.y_data_min + y_fraction * (self.y_data_max - self.y_data_min)
        return x_data, y_data
