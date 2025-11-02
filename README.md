# GoPro-Metadata-Extractor

## Description
A small toolchain to upload a GoPro MP4 video, extract embedded GPMF metadata (GPS, accelerometer and gyroscope), and convert the extracted streams into readable CSV files ready for further processing. The original GPMF_demo.c was modified to extract GPS, accelerometer and gyrometer metadata. The extracted raw metadata is then processed with Python (pandas) to produce clean CSV outputs.

## Features
- Extract GPMF metadata from GoPro-recorded MP4 files (GPS, accelerometer, gyroscope).
- Modified version of GPMF_demo.c performs the low-level extraction.
- Python/pandas pipeline converts extracted data into human-readable CSV files ready for analysis.

## Project structure (suggested)
- GPMF_demo.c (modified) — C program to extract GPMF metadata from MP4
- extract_metadata.sh / build script — optional helper to build/run the extractor
- process_metadata.py — Python script that parses extracted output and writes CSV
- requirements.txt — Python deps (e.g., pandas)
- README.md — this file

## Quickstart
1. Build the C extractor (example):
    - gcc -o gpmf_extractor GPMF_demo.c
2. Extract metadata from a GoPro MP4:
    - ./gpmf_extractor path/to/input.mp4 path/to/output.raw
3. Prepare Python environment and install requirements:
    - python3 -m venv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
4. Convert the raw metadata to CSV:
    - python process_metadata.py --input path/to/output.raw --output path/to/output.csv

## Output CSV (typical columns)
- timestamp
- gps_latitude, gps_longitude, gps_altitude
- accel_x, accel_y, accel_z
- gyro_x, gyro_y, gyro_z
(Actual columns depend on how process_metadata.py maps and parses the GPMF streams.)

## Notes
- The modified GPMF_demo.c focuses on extracting GPS, accelerometer and gyrometer streams; further post-processing (resampling, unit conversion, interpolation) is done in Python using pandas.
- Adjust compile flags and dependencies according to your platform and the original GPMF demo requirements.

## Contributing
- Fixes, improvements and better CSV schemas welcome. Include test MP4 samples or sample outputs when submitting changes.

## License
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.