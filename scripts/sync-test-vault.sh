#!/bin/sh
# Copies theme.css and manifest.json into the test vault, for systems where
# the symlinks in test-vault/.obsidian/themes/Fallout don't work (e.g. Windows
# without developer mode). Rebuilds theme.css first.
set -e
cd "$(dirname "$0")/.."
python3 scripts/build.py
dest=test-vault/.obsidian/themes/Fallout
rm -f "$dest/theme.css" "$dest/manifest.json"
cp theme.css manifest.json "$dest/"
echo "Copied into $dest"
