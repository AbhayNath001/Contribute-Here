import requests

Api_Key = "dFVeOEqeeJijlEJWyRUks6emx10P5JZfwKMiv7jU"

print("Be sure that the starting and ending date range must be under the 7 days")
start_date = input("Enter the starting date [yyyy-mm-dd]: ")
end_date = input("Enter the ending date [yyyy-mm-dd]: ")

try:
    print("Collecting Data...")
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
    r = requests.get(url)
    Data = r.json()
    Total_Astro = Data['element_count']
    neo = Data['near_earth_objects']
    print(f"\nTotal Astroids between from {start_date} to {end_date} is: {Total_Astro}")
    magnitudes = []
    max_magnitude = float('-inf')
    min_magnitude = float('inf')
    max_asteroid_name = ""
    min_asteroid_name = ""
    for body in neo[start_date]:
        name = body['name']
        absolute = body['absolute_magnitude_h']
        magnitudes.append(absolute)
        if absolute > max_magnitude:
            max_magnitude = absolute
            max_asteroid_name = name
        if absolute < min_magnitude:
            min_magnitude = absolute
            min_asteroid_name = name
        print(f"\nName: {name} \n\tAbsolute Magnitude: {absolute}")
    if magnitudes:
        print(f"\nMaximum absolute magnitude: {max_magnitude}")
        print(f"Corresponding asteroid name: {max_asteroid_name}")
        print(f"Minimum absolute magnitude: {min_magnitude}")
        print(f"Corresponding asteroid name: {min_asteroid_name}")
    else:
        print("No asteroids found.")
except:
    print("Be sure the difference between starting date and ending date is not more than 7 days.")

