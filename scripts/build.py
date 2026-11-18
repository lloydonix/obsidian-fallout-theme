#!/usr/bin/env python3
"""Assemble theme.css from src/theme.src.css, embedding fonts/*.woff2 as base64."""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FACES = [  # family, style, weight, file
    ("Share Tech Mono", "normal", 400, "ShareTechMono-Regular.woff2"),
    ("JetBrains Mono", "normal", 400, "JetBrainsMono-Regular.woff2"),
    ("JetBrains Mono", "italic", 400, "JetBrainsMono-Italic.woff2"),
    ("JetBrains Mono", "normal", 700, "JetBrainsMono-Bold.woff2"),
    ("JetBrains Mono", "italic", 700, "JetBrainsMono-BoldItalic.woff2"),
]

def face(family, style, weight, name):
    data = base64.b64encode((ROOT / "fonts" / name).read_bytes()).decode()
    return (f'@font-face {{ font-family: "{family}"; font-style: {style}; font-weight: {weight}; '
            f'font-display: swap; src: url(data:font/woff2;base64,{data}) format("woff2"); }}')

src = (ROOT / "src" / "theme.src.css").read_text()
out = src.replace("/*@@FONTS@@*/", "\n".join(face(*f) for f in FACES))
(ROOT / "theme.css").write_text(out)
print(f"theme.css: {len(out):,} bytes")

# Obsidian watches the vault's theme folder, not the symlink's target, so a
# rebuilt theme.css only reloads when the link itself is recreated.
link = ROOT / "test-vault" / ".obsidian" / "themes" / "Fallout" / "theme.css"
if link.is_symlink():
    target = link.readlink()
    link.unlink()
    link.symlink_to(target)
