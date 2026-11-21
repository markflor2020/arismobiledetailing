#!/usr/bin/env python3
"""Make responsive WebP copies of every photo in assets/img/.

For each source photo (photo.jpg / photo.png) this writes photo-<width>.webp at a
few widths, never upscaling. Pages reference them with srcset/sizes, e.g.

  <img src="assets/img/photo-960.webp"
       srcset="assets/img/photo-480.webp 480w, assets/img/photo-960.webp 960w"
       sizes="(min-width: 981px) 370px, 92vw" width="960" height="1280" ...>

Idempotent: only (re)builds a variant when it's missing or older than its source.
The original JPG/PNG is kept (the hero JPG is the social-share image).

Usage:  python3 optimize_images.py      (needs Pillow: pip3 install Pillow)
"""
import pathlib
from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).parent
IMG = ROOT / "assets" / "img"
QUALITY = 76


def widths_for(src_w):
    """Widths to generate for a source this wide: 480 + 960 for typical photos,
    more steps for wide/hero shots, plus the native width when it's > 960."""
    if src_w <= 960:
        ws = [480, src_w] if src_w > 480 else [src_w]
    else:
        ws = [640, 960, src_w] if src_w <= 1280 else [640, 960, 1280]
    return sorted(set(w for w in ws if w <= src_w))


def main():
    built = skipped = 0
    for src in sorted(p for p in IMG.iterdir() if p.suffix.lower() in (".jpg", ".jpeg", ".png")):
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)  # match how browsers display it
            if im.mode not in ("RGB", "RGBA"):
                im = im.convert("RGB")
            for w in widths_for(im.width):
                out = IMG / f"{src.stem}-{w}.webp"
                if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
                    skipped += 1
                    continue
                h = round(im.height * w / im.width)
                im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=QUALITY, method=6)
                built += 1
                print(f"  {out.name:34} {w}x{h}  {out.stat().st_size // 1024} KiB")
    print(f"done: {built} built, {skipped} up to date")


if __name__ == "__main__":
    main()
