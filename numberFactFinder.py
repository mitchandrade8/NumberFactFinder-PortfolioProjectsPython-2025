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
    
def main():
    print("--- Number Fact Finder ---")

    # Loop: The program runs continuously until the user quits
    while True:
        try:
            # Input: Get input from the user
            user_input = input("Enter a positive integer (or 'q' to quit): ")

            if user_input.lower() == 'q':
                print("Exiting application. Goodbye!")
                break # Break out of the while loop to end the program

            # Input and Validation: Convert the input to an integer
            number = int(user_input)

            if number < 0:
                print("Please enter a positive integer.")
                continue # Skip the rest of the loop and ask for input again

            # Calling the Logic: Run the function that handles the API call
            fact_result = get_number_fact(number)

            # Output: Print the result clearly
            print("-" * 40)
            print(f"Fact for {number}:")
            print(fact_result)
            print("-" * 40)

        except ValueError:
            # Handles non-numeric input that wasn't 'q'
            print("Invalid input. Please enter a whole number or 'q'.")
        except KeyboardInterrupt:
            # Allows user to exit gracefully with Ctrl+C
            print("\nExiting application. Goodbye!")
            sys.exit(0)
