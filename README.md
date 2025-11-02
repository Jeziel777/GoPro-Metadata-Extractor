# GoPro-Metadata-Extractor

## Description
A small toolchain to upload a GoPro MP4 video, extract embedded GPMF metadata (GPS, accelerometer, and gyroscope), and convert the extracted streams into readable CSV files ready for further processing.  

The original [GPMF-Parser](https://github.com/gopro/gpmf-parser.git) project by GoPro was used as a base, with a modified `GPMF_demo.c` file to extract GPS, accelerometer, and gyroscope metadata. The extracted raw metadata is then processed with Python (pandas) to produce clean CSV outputs.

---

<p align="center">
  <img src="assets\simple webpage.png" width="800"/>
</p>

## Credits
This project builds upon and uses the **GPMF-Parser** open-source project by GoPro:  
🔗 [https://github.com/gopro/gpmf-parser.git](https://github.com/gopro/gpmf-parser.git)

---

## Features
- Extract GPMF metadata from GoPro-recorded MP4 files (GPS, accelerometer, gyroscope).
- Modified version of `GPMF_demo.c` performs low-level metadata extraction.
- Python/pandas pipeline converts extracted data into human-readable CSV files ready for analysis.

---

## Important Files
- `C-code/demo/GPMF_demo.c` — modified C program to extract GPMF metadata from MP4.

---

## Setup & Running Instructions


### 1. Build the GPMF Parser

Run the following commands to build the C extractor inside C-code folder

```bash
mkdir cvs_extractor
cd cvs_extractor
cmake ..
make
```

---

### 4. Run the Web Application

Once the C extractor is built, run the Python web interface:

```bash
python app.py
```

This will launch a local web page that allows you to upload GoPro `.mp4` files.  
The uploaded videos will be processed, and the extracted metadata will be saved as `.csv` files.

---

## Output CSV (Typical Columns)

- `timestamp`
- `gps_latitude`, `gps_longitude`, `gps_altitude`
- `accel_x`, `accel_y`, `accel_z`
- `gyro_x`, `gyro_y`, `gyro_z`

(Actual columns depend on how `process_metadata.py` maps and parses the GPMF streams.)

---

## Notes

- The modified `GPMF_demo.c` focuses on extracting GPS, accelerometer, and gyroscope streams.  
- Post-processing (resampling, unit conversion, interpolation) is done in Python using pandas.  
- Adjust compile flags and dependencies according to your platform and the original GPMF demo requirements.

---

## Contributing

Fixes, improvements, and better CSV schemas are welcome.  
Include test MP4 samples or sample outputs when submitting changes.

---

## License

Apache License, Version 2.0 (`LICENSE-APACHE`)  
MIT License (`LICENSE-MIT`)

