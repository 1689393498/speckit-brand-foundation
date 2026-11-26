#!/usr/bin/env python3
"""Build a distributable Brand extension archive.

Usage:
    python scripts/package.py

Produces:
    dist/brand-foundation-<version>.zip
    dist/brand-foundation-<version>.zip.sha256
"""

from __future__ import annotations

import hashlib
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
INCLUDE_FILES = [
    "extension.yml",
    "README.md",
    "README.en.md",
    "CHANGELOG.md",
    "LICENSE",
]
INCLUDE_DIRS = ["commands"]


def read_version() -> str:
    text = (ROOT / "extension.yml").read_text(encoding="utf-8")
    try:
        extension_block = text.split("extension:", 1)[1].split("requires:", 1)[0]
    except IndexError:
        raise SystemExit("extension.yml: 找不到 extension 或 requires 段")

    match = re.search(
        r'^\s*version:\s*["\']?([^"\'\s]+)', extension_block, re.MULTILINE
    )
    if not match:
        raise SystemExit("extension.yml: 找不到 extension.version")
    return match.group(1)


def collect_files() -> list[Path]:
    files: list[Path] = []
    for name in INCLUDE_FILES:
        path = ROOT / name
        if not path.is_file():
            raise SystemExit(f"缺少文件: {name}")
        files.append(path)

    for dirname in INCLUDE_DIRS:
        base = ROOT / dirname
        if not base.is_dir():
            raise SystemExit(f"缺少目录: {dirname}")
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            if "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            files.append(path)

    return files


def main() -> None:
    version = read_version()
    DIST.mkdir(exist_ok=True)
    archive = DIST / f"brand-foundation-{version}.zip"
    if archive.exists():
        archive.unlink()

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in collect_files():
            zf.write(path, path.relative_to(ROOT).as_posix())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum = archive.with_suffix(archive.suffix + ".sha256")
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="utf-8")

    print(f"Archive:  {archive}")
    print(f"SHA-256:  {digest}")
    print(f"Checksum: {checksum}")
    print("Upload the .zip to an HTTPS host and share the URL.")


if __name__ == "__main__":
    main()
