#!/usr/bin/env python3
"""Render the downloadable PDF and images for the site.

Usage:  python3 build/render_downloads.py   (run after build/build_site.py)
Writes  site/downloads/ai-risk-map.pdf, site/downloads/ai-risk-map-<name>.pdf, site/img/<name>.png
"""
import subprocess, pathlib
from PIL import Image, ImageChops

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BG = (233, 236, 240)  # infographic page background (#e9ecf0)

def chrome(*args):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=10000", *args],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    (SITE / "downloads").mkdir(exist_ok=True)
    (SITE / "img").mkdir(exist_ok=True)
    pdf = SITE / "downloads" / "ai-risk-map.pdf"
    chrome(f"--print-to-pdf={pdf}", "--no-pdf-header-footer", (SITE / "index.html").as_uri() + "?print")
    print("wrote", pdf.relative_to(ROOT), pdf.stat().st_size // 1024, "KB")
    summ = SITE / "downloads" / "ai-risk-map-summary.pdf"
    chrome(f"--print-to-pdf={summ}", "--no-pdf-header-footer", (SITE / "index.html").as_uri() + "?bare")
    print("wrote", summ.relative_to(ROOT), summ.stat().st_size // 1024, "KB")
    for name in ("poster", "landscape", "anatomy"):
        png = SITE / "img" / f"{name}.png"
        chrome("--force-device-scale-factor=2", "--window-size=1240,3400", f"--screenshot={png}", (SITE / f"{name}.html").as_uri() + "?bare")
        im = Image.open(png).convert("RGB")
        box = ImageChops.difference(im, Image.new("RGB", im.size, BG)).point(lambda v: 255 if v > 8 else 0).getbbox()
        if box:
            im = im.crop((0, 0, im.width, min(im.height, box[3] + 48)))
        im.save(png, optimize=True)
        out = SITE / "downloads" / f"ai-risk-map-{name}.pdf"
        im.save(out, "PDF", resolution=144)
        print("wrote", png.relative_to(ROOT), im.size, "and", out.relative_to(ROOT))

if __name__ == "__main__":
    main()
