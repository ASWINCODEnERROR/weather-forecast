import requests
from datetime import datetime

def get_weather_forecast(api_key, city, time):
    # Convert the input time to UTC timestamp
    timestamp = int(datetime.strptime(time, '%Y-%m-%d %H:%M:%S').timestamp())

    # OpenWeatherMap API endpoint for 3-Hour Forecast 5 days
    endpoint = "http://api.openweathermap.org/data/2.5/forecast"
    
    
    
    # API parameters
    params = {
        'q': city,
        'appid': api_key,
        'cnt': 40,  # Request 40 data points to cover 5 days with 3-hour intervals
    }


    # Make the API request
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()

        # Find the closest forecast time to the specified time
        closest_forecast = min(data['list'], key=lambda x: abs(x['dt'] - timestamp))

        # Print the weather information for the specified time
        print(f"Weather forecast for {city} at {time}:")
        print(f"Temperature: {closest_forecast['main']['temp']}°C")
        print(f"Description: {closest_forecast['weather'][0]['description']}")
        print(f"Wind Speed: {closest_forecast['wind']['speed']} m/s")
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    # api_key = 'ab0a38bd53dc48271141584b808cc3b9'
    api_key = 'e4dc53ac469bb81befdae7bda946d3e4'
    
    
    
    # Specify the city and time for the weather forecast
    city = 'Calicut'
    input_time = input("Enter the specific time (YYYY-MM-DD HH:MM:SS): ")

    # Call the function to get the weather forecast
    get_weather_forecast(api_key, city, input_time)
