"""CLI for agent-color-contrast-wcag-auditor."""
import argparse
import sys
from .core import ColorContrastAuditor, RgbColor

def main():
    parser = argparse.ArgumentParser(description="Agent Color Contrast WCAG Auditor CLI")
    parser.add_argument("--demo", action="store_true", help="Run color contrast audit demo")
    args = parser.parse_args()

    if args.demo:
        auditor = ColorContrastAuditor()
        pairs = [
            ("#000000", "#FFFFFF", "Black on White"),
            ("#71717A", "#FFFFFF", "Muted Gray on White"),
            ("#F59E0B", "#FFFFFF", "Yellow on White")
        ]
        for fg_hex, bg_hex, desc in pairs:
            fg = RgbColor.from_hex(fg_hex)
            bg = RgbColor.from_hex(bg_hex)
            cr = auditor.calculate_contrast(fg, bg)
            print(f"[+] {desc} ({fg_hex} / {bg_hex}): Ratio = {cr.ratio}:1 (AA: {cr.passes_aa}, AAA: {cr.passes_aaa})")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
