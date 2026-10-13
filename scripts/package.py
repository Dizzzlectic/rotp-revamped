#!/usr/bin/env python3
"""Package the mod payload using the name and version in src/mod.json."""

import json
from pathlib import Path
import re
import shutil
import tempfile


def main():
    project = Path(__file__).resolve().parents[1]
    source = project / "src"
    manifest = json.loads((source / "mod.json").read_text(encoding="utf-8"))
    name = manifest["name"]
    version = manifest["version"]
    for field, value in (("name", name), ("version", version)):
        if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]*", value):
            raise ValueError(f"mod.json {field} must be a non-empty filename-safe string")

    destination = project / "dist"
    destination.mkdir(exist_ok=True)
    output = destination / f"{name}-{version}.zip"
    with tempfile.TemporaryDirectory(prefix=".package-", dir=destination) as temporary:
        staging = Path(temporary)
        payload = staging / name
        shutil.copytree(source, payload)
        shutil.copyfile(project / "LICENSE", payload / "LICENSE")
        archive = shutil.make_archive(
            str(staging / f"{name}-{version}"), "zip", root_dir=staging, base_dir=name
        )
        Path(archive).replace(output)

    print(output)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        raise SystemExit(f"Packaging failed: {error}")
