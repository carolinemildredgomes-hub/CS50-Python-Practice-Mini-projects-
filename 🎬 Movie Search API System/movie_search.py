import requests

movie_name = input("Enter movie name: ")

url = "https://www.omdbapi.com/?apikey=564727fa&s=" + movie_name

response = requests.get(url)

data = response.json()

if data["Response"] == "True":
    print("\nMovie Results:\n")
    for movie in data["Search"]:
        print(movie["Title"])
else:
    print("No movie found.")
