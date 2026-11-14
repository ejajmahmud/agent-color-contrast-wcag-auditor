"""Core color contrast WCAG auditor implementation."""
from typing import Tuple

class RgbColor:
    def __init__(self, r: int, g: int, b: int):
        self.r = max(0, min(255, r))
        self.g = max(0, min(255, g))
        self.b = max(0, min(255, b))

    @classmethod
    def from_hex(cls, hex_str: str) -> "RgbColor":
        h = hex_str.strip().lstrip("#")
        if len(h) == 3:
            h = "".join(c*2 for c in h)
        val = int(h, 16)
        return cls((val >> 16) & 255, (val >> 8) & 255, val & 255)

    @property
    def relative_luminance(self) -> float:
        # WCAG sRGB luminance formula
        def channel_lum(val: int) -> float:
            c = val / 255.0
            return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * channel_lum(self.r) + 0.7152 * channel_lum(self.g) + 0.0722 * channel_lum(self.b)

class ContrastRatio:
    def __init__(self, ratio: float):
        self.ratio = ratio

    @property
    def passes_aa(self) -> bool:
        return self.ratio >= 4.5

    @property
    def passes_aaa(self) -> bool:
        return self.ratio >= 7.0

class ColorContrastAuditor:
    @staticmethod
    def calculate_contrast(c1: RgbColor, c2: RgbColor) -> ContrastRatio:
        l1 = c1.relative_luminance
        l2 = c2.relative_luminance
        lighter = max(l1, l2)
        darker = min(l1, l2)
        ratio = (lighter + 0.05) / (darker + 0.05)
        return ContrastRatio(round(ratio, 2))
