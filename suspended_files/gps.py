import piexif
from fractions import Fraction

def extract_gps_coordinates(image_path):
    try:
        # Load the EXIF data from the image
        exif_data = piexif.load(image_path)

        # Check if GPSInfo exists in the EXIF data
        if "GPS" in exif_data and piexif.GPSIFD.GPSLatitude in exif_data["GPS"]:
            latitude = exif_to_decimal(exif_data["GPS"][piexif.GPSIFD.GPSLatitude])
            longitude = exif_to_decimal(exif_data["GPS"][piexif.GPSIFD.GPSLongitude])

            # Check latitude and longitude references for negative values
            latitude_ref = exif_data["GPS"][piexif.GPSIFD.GPSLatitudeRef]
            if latitude_ref == "S":
                latitude = -latitude

            longitude_ref = exif_data["GPS"][piexif.GPSIFD.GPSLongitudeRef]
            if longitude_ref == "W":
                longitude = -longitude

            return latitude, longitude

    except Exception as e:
        print(f"Error extracting GPS coordinates: {str(e)}")

    return None


def exif_to_decimal(coord):
    degrees = coord[0][0] / coord[0][1]
    minutes = coord[1][0] / coord[1][1]
    seconds = coord[2][0] / coord[2][1]
    return degrees + (minutes / 60.0) + (seconds / 3600.0)


# Provide the path to the photo file you want to analyze
image_path = 'IMG_1421.jpg'

# Call the function to extract GPS coordinates
gps_coordinates = extract_gps_coordinates(image_path)

# Display the resulting coordinates
if gps_coordinates:
    latitude, longitude = gps_coordinates
    print(f"Latitude,Longitude {latitude},{longitude}")
else:
    print("No GPS coordinates found.")