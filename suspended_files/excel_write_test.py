import openpyxl

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

if __name__ == "__main__":
    # Example data to append (list of lists, where each sublist represents a row)
    data_to_append = [
        ["John", 30, "Engineer"],
        ["Alice", 28, "Designer"],
        ["Bob", 32, "Manager"]
    ]

    # Replace 'your_file_path.xlsx' with the path to your Excel file
    file_path = 'site_data.xlsx'

    # Call the function to append data
    append_to_excel(file_path, data_to_append)
