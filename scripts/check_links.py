#!/usr/bin/env python3
"""Comprueba que los enlaces relativos de los documentos Markdown existen.

No sale a Internet: solo valida rutas dentro del repositorio. Los enlaces
absolutos, los anclas y el correo se ignoran.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "node_modules"}
LINK = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^)\s]+))")

def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if not (SKIP & set(path.relative_to(ROOT).parts))
    ]

def targets(text: str):
    for angle, plain in LINK.findall(text):
        yield (angle or plain).strip()

def main() -> int:
    missing: list[tuple[Path, str]] = []
    for path in markdown_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in targets(text):
            parsed = urlparse(target)
            if parsed.scheme or target.startswith(("#", "mailto:", "tel:")):
                continue
            clean = unquote(parsed.path)
            if not clean:
                continue
            if not (path.parent / clean).resolve().exists():
                missing.append((path.relative_to(ROOT), target))

    if missing:
        for path, target in missing:
            print(f"{path}: {target}")
        print(f"\n{len(missing)} enlaces relativos rotos")
        return 1

    print(f"OK: {len(markdown_files())} documentos sin enlaces relativos rotos")
    return 0

if __name__ == "__main__":
    sys.exit(main())
