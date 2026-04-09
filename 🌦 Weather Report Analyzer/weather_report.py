import requests


def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"City: {city}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description']}")
    else:
        print("City not found.")


def main():
    city = input("Enter city name: ")
    get_weather(city)


if __name__ == "__main__":
    main()
