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

    except Exception as e:
        return f"An unexpected internal error occurred: {e}"