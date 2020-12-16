# simpleMusicMatcher

This is a simple music matcher leveraging AcoustID's Chromaprint. Scans recursively through a given path and then looks for duplicate files.

## Features:
- Stores fingerprints in a SQLite DB
- That's all really...

## Requires:
- Python 3
- AcoustID's fpcalc and Chromaprint Python library

## Installation:
1. Download this source and extract somewhere.
2. Install fpcalc
   - On Debian/Ubuntu: `apt-get install libchromaprint-tools` (Other Linux distros have their own packages as well.)
   - On Windows: Download the latest fpcalc from https://acoustid.org/chromaprint and extract it to script folder.
3. Then: `pip install pyacoustid`

## Usage:
`python matcher_main.py <path to your music library>`

