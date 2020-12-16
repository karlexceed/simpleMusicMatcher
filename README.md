# simpleMusicMatcher

This is a simple music matcher leveraging AcoustID's Chromaprint.

## Features:
- Stores fingerprints in a SQLite DB
- That's all really...

## Requires:
- Python 3
- AcoustID's fpcalc and Chromaprint Python library

## Installation:
Download this source and extract somewhere.

- On Debian/Ubuntu: `apt-get install libchromaprint-tools` (Other Linux distros have their own packages as well.)
- On Windows: Download the latest fpcalc from https://acoustid.org/chromaprint and extract it to script folder.

Then: `pip install pyacoustid`

## Usage:
`python matcher_main.py <path to your music library>`

