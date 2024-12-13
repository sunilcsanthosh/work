import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
import boto3
import piexif
from fractions import Fraction
import openpyxl

def upload_file():
    global img
    aws_mag_con = boto3.session.Session(profile_name ='Anumol')
    client = aws_mag_con.client(service_name ='textract',region_name = 'us-east-1')

    f_types = [('Jpg Files',"*.jpg")]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    print ( f"file location :{filename}")
    
    try:
        with open(filename ,'rb') as file:
            img = Image.open(filename)
        # Process the image as needed
    except IOError as e:
        print("Error: Unable to open the image file -", e)
    #resigning Image
    
    img_resize =img.resize((850,600))
    img=ImageTk.PhotoImage(img_resize)

    # Convert Image in byte
    imgbytes =get_image_byte(filename)

    b2 =tk.Button(my_window,image=img)
    b2.pack()

    # Call the function to extract GPS coordinates
    gps_coordinates = extract_gps_coordinates(filename)

    # Display the resulting coordinates
    if gps_coordinates:
        latitude, longitude = gps_coordinates
        print(f"Site GPS cordinates details : Latitude,Longitude {latitude},{longitude}")
    else:
        print("No GPS coordinates found.")

    # Initialize an empty string to store the combined text
    combined_text = ""
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract/client/detect_document_text.html
    response = client.detect_document_text(Document={'Bytes':imgbytes})
    for item in response['Blocks']:
        if item['BlockType']=='LINE':
            #print(item['Text'])
            combined_text += item['Text'] + "\n"
    
    print(combined_text)

    # Calling google map link function 
    google_maps_link = generate_google_maps_link(latitude, longitude)

    # Example data to append (list of lists, where each sublist represents a row)
    data_to_append = [
        ["Site GPS cordinates details",google_maps_link,latitude,longitude, combined_text]
                    ]

    # Replace 'your_file_path.xlsx' with the path to your Excel file
    file_path = 'site_data.xlsx'

    # Call the function to append data
    append_to_excel(file_path, data_to_append)




def get_image_byte(filename):
    with open(filename,'rb') as imagfile:
        return imagfile.read()


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

def append_to_excel(file_path, data_to_append):
    # Load the existing workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the active sheet (you can choose a specific sheet by name or index)
    sheet = workbook.active

    # Find the last row with data in the sheet
    last_row = sheet.max_row + 1

    # Append the data to the sheet
    for row_data in data_to_append:
        sheet.append(row_data)

    # Save the changes
    workbook.save(file_path)
    print("Data appended successfully!")

# Generating google map link
def generate_google_maps_link(latitude, longitude):
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    return google_maps_link



my_window = tk.Tk()
my_window.geometry("850x600")
my_window.title("Xylem Data Plate Textract- by Sunil Santhosh")
l1 = tk.Label(my_window,text= "Please upload the pump dataplate photo ", width=30, font= ('times',18,'bold'))
l1.pack()

b1 =tk.Button(my_window,text= 'Upload File & See what it has!!!!',width=30, command =lambda: upload_file())
b1.pack()


my_window.mainloop()
