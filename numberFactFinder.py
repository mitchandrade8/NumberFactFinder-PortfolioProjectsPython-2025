import requests
import sys

#Global API
API_URL = "http://numbersapi.com"

# Get number function
def get_number_fact(number):
    
    endpoint = f"{API_URL}\{number}/trivia"

    print(f"\nSearching for a fact about {number}...")

    try:
        response = requests.get(endpoint)

        response.raise_for_status()

        fact = response.text
        return fact

    except requests.exceptions.HTTPError as errh:
        # Handles 400/500 level errors (e.g., Not Found, Server Error)
        return f"HTTP Error occurred: {errh}"
    except requests.exceptions.ConnectionError as errc:
        # Handles network issues (e.g., DNS failure, refused connection)
        return f"Error Connecting (Is your internet working?): {errc}"
    except requests.exceptions.Timeout as errt:
        # Handles request timeouts
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        # Handles all other general request errors
        return f"An unknown error occurred during the API request: {err}"
    except Exception as e:
        return f"An unexpected internal error occurred: {e}"