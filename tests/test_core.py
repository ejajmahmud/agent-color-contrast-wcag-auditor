"""Unit tests for agent-color-contrast-wcag-auditor."""
import unittest
from agent_color_contrast_wcag_auditor.core import ColorContrastAuditor, RgbColor

class TestColorContrastAuditor(unittest.TestCase):
    def test_black_on_white_maximum_contrast(self):
        c_black = RgbColor(0, 0, 0)
        c_white = RgbColor(255, 255, 255)
        res = ColorContrastAuditor.calculate_contrast(c_black, c_white)
        self.assertEqual(res.ratio, 21.0)
        self.assertTrue(res.passes_aa)
        self.assertTrue(res.passes_aaa)

    def test_from_hex(self):
        c = RgbColor.from_hex("#ff0000")
        self.assertEqual((c.r, c.g, c.b), (255, 0, 0))
