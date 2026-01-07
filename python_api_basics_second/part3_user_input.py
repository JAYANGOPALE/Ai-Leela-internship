"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

import requests


def get_user_info():
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")

    if not user_id.isdigit():
        print("\nError: Please enter a valid numeric user ID.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    """Search posts by user ID."""
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ")

    if not user_id.isdigit():
        print("\nError: Please enter a valid numeric user ID.")
        return

    # Using query parameters
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")

def get_weather_by_city():
    """Fetch current weather for a specific city."""
    print("\n=== Weather Checker ===\n")

    city = input("Enter city name (e.g., London, Tokyo): ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    # Step 1: Get coordinates (Geocoding)
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city, "count": 1, "language": "en", "format": "json"}

    try:
        geo_response = requests.get(geo_url, params=geo_params)
        geo_data = geo_response.json()

        if "results" not in geo_data:
            print(f"City '{city}' not found.")
            return

        location = geo_data["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        name = location["name"]
        country = location.get("country", "")

        print(f"Found: {name}, {country}")

        # Step 2: Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": "true"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        current = weather_data.get("current_weather", {})
        temp = current.get("temperature", "N/A")
        wind = current.get("windspeed", "N/A")

        print(f"\n--- Weather in {name} ---")
        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {wind} km/h")

    except Exception as e:
        print(f"An error occurred: {e}")

def search_todos():
    """Search todos by completion status."""
    print("\n=== Todo Search ===\n")

    status = input("Search for completed todos? (y/n): ").lower().strip()
    
    if status == 'y':
        completed = "true"
    elif status == 'n':
        completed = "false"
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": completed}

    response = requests.get(url, params=params)
    todos = response.json()

    if todos:
        status_text = "Completed" if completed == "true" else "Incomplete"
        print(f"\n--- {status_text} Todos (First 10) ---")
        for i, todo in enumerate(todos[:10], 1):
            print(f"{i}. {todo['title']}")
    else:
        print("No todos found.")

def main():
    """Main menu for the program."""
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Check city weather")
        print("5. Search todos")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_weather_by_city()
        elif choice == "5":
            search_todos()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)
