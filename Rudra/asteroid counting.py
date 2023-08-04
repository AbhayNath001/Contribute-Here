import datetime
import requests
import webbrowser

def get_universe_info(date):
    print("collecting...")
    url = "https://api.nasa.gov/planetary/apod"
    api_key = "Spv4WWgql5WKmuDMEzcphd6Rro7zcQSx9mYN4xhX"
    params = {"api_key": api_key, "date": date}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        title = data["title"]
        explanation = data["explanation"]
        image_url = data["url"]
        webbrowser.open(image_url, new=2, autoraise=True)
        print(f"On {date}, the main topic of our universe was: {title}\n{explanation}\nImage URL: {image_url}")
    else:
        print("Sorry, I could not retrieve information about the universe for that date.")

def ApiExecution(tag, query):
    if "asteroid_count" in tag:
        Api_Key = "dFVeOEqeeJijlEJWyRUks6emx10P5JZfwKMiv7jU"

        print("Be sure that the starting and ending date range must be under 7 days")
        start_date = input("Enter the starting date [yyyy-mm-dd]: ")
        end_date = input("Enter the ending date [yyyy-mm-dd]: ")

        try:
            print("Collecting Data...")
            url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"
            r = requests.get(url)
            Data = r.json()
            Total_Astro = Data['element_count']
            neo = Data['near_earth_objects']
            print(f"\nTotal Asteroids between {start_date} and {end_date} is: {Total_Astro}")
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
                print(f"The brightest asteroid was {min_asteroid_name} with an absolute magnitude of: {min_magnitude}")
                print(f"The most dimmed asteroid was {max_asteroid_name} with an absolute magnitude of: {max_magnitude}")
            else:
                print("No asteroids found.")
        except:
            print("Be sure the difference between the starting date and ending date is not more than 7 days.")
            
    elif "universe_news" in tag:
        date = input("Enter a date (yyyy-mm-dd): ")
        get_universe_info(date)

# Example usage:
ApiExecution("universe_news", "")
