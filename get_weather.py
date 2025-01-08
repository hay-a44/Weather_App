import requests
api_key = "f96804604415a7ca34ee5a5989336d6a"
def get_weather(city_name, api_key):
    # OpenWeatherMap API endpoint for current weather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    # Send the request to the API
    response = requests.get(url)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()

        # Return the weather data as a dictionary
        return {
            'city': data["name"],
            'country': data["sys"]["country"],
            'temperature': data["main"]["temp"],
            'weather_description': data["weather"][0]["description"],
            'humidity': data["main"]["humidity"],
            'wind_speed': data["wind"]["speed"]
        }
    else:
        print(f"Failed to get weather data. HTTP Status code: {response.status_code}")
        return None

