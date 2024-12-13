# Data Plate Textract Tool

## Overview
This tool allows users to upload an image of a pump data plate, extract GPS coordinates embedded in the image's EXIF data, and process text data using AWS Textract. It also appends the extracted data to an Excel file for further use.

---

## Features
- **Image Upload:** Users can upload `.jpg` files using a GUI.
- **GPS Extraction:** Extracts GPS coordinates from EXIF metadata of the uploaded image.
- **Text Extraction:** Uses AWS Textract to extract textual information from the image.
- **Google Maps Link:** Generates a Google Maps link for the extracted GPS coordinates.
- **Excel Integration:** Appends extracted data (GPS, text, Google Maps link) to an Excel file (`site_data.xlsx`).
- **Responsive GUI:** Built with `Tkinter` for a user-friendly interface.

---

## Requirements
### Python Libraries
Install the following Python libraries:
- `tkinter` (comes pre-installed with Python)
- `boto3`
- `Pillow`
- `piexif`
- `openpyxl`

Run the following command to install required libraries:
```bash
pip install boto3 Pillow piexif openpyxl
```

### AWS Configuration
- Set up an AWS account.
- Create an IAM user with `Textract` permissions.
- Configure AWS CLI with the profile name `Anumol` (or update the script with your AWS profile).

### File Requirements
- Ensure `site_data.xlsx` exists in the script directory. It should have the required headers.

---

## How to Use
### Step 1: Launch the Application
Run the script to open the GUI:
```bash
python script_name.py
```

### Step 2: Upload an Image
1. Click the button `Upload File & See what it has!!!!`.
2. Select a `.jpg` file from your system.

### Step 3: View Results
- The script extracts:
  - **GPS Coordinates:** Prints Latitude and Longitude in the console.
  - **Text Data:** Displays extracted text from AWS Textract in the console.
  - **Google Maps Link:** Prints a link to the GPS coordinates in the console.

### Step 4: Data Storage
- The extracted data is appended to `site_data.xlsx` in the following format:
  | Column                  | Data                                             |
  |-------------------------|--------------------------------------------------|
  | Site GPS Coordinates    | Google Maps link to the location                 |
  | Latitude                | Extracted Latitude                               |
  | Longitude               | Extracted Longitude                              |
  | Extracted Text          | Combined text extracted using AWS Textract       |

---

## Functions
### `upload_file()`
Handles file selection, image processing, GPS extraction, text extraction, and data appending to Excel.

### `get_image_byte(filename)`
Converts an image file into bytes for AWS Textract processing.

### `extract_gps_coordinates(image_path)`
Extracts GPS metadata from the EXIF data of the uploaded image.

### `exif_to_decimal(coord)`
Converts GPS coordinates from EXIF format to decimal format.

### `generate_google_maps_link(latitude, longitude)`
Generates a Google Maps link using extracted GPS coordinates.

### `append_to_excel(file_path, data_to_append)`
Appends extracted data to an Excel file.

---

## Notes
- Ensure the `site_data.xlsx` file exists and is not open while the script is running.
- Update AWS profile credentials if necessary.
- Handle error messages in the console for troubleshooting.

---

## License
This tool is developed by Sunil Cheeremvelil Santhosh for personal and professional use.

