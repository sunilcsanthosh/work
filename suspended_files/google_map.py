def generate_google_maps_link(latitude, longitude):
    google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    return google_maps_link

# Example usage
latitude = 25.135783333333332
longitude = 55.23911666666667
google_maps_link = generate_google_maps_link(latitude, longitude)
print(google_maps_link)
