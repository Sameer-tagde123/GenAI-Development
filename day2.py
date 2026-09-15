# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print("Result:", result)
# except ValueError:
#     print("That’s not a valid number!")
# except ZeroDivisionError:
#     print("You can’t divide by zero!")
# except Exception as e:
#     print("Something went wrong:", e)
# finally:
#     print("This always runs.")

# ------------------------------------------------------------------------------------------------------------------------------

# Exercise 1

# Write a function safe_divide(a, b) that:

# Tries to divide a by b
# Returns the result if successful
# Returns the message "Cannot divide by zero" if b is 0
# Returns "Invalid input" if the values are not numbers

# Test it with different inputs.
# ------------------------------------------------------------------------------------------------------------------------------

# try:
    
#     a=int (input("enter the value of a: "))
#     b=int (input("enter the value of b: "))
#     result=a/b

#     if result<=0:
#         print("kindly enter the numbers correctly")
    
#     print(result)

# except ZeroDivisionError:
#     print("can not devide by zero" ) 
# except ValueError:
#     print("Invalid input")       
# finally:
#     print("thank you for using my code")    

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6]

# # Traditional way
# squares = []
# for n in numbers:
#     squares.append(n ** 2)

# # Modern way (comprehension)
# squares = [n ** 2 for n in numbers]
# even_squares = [n ** 2 for n in numbers if n % 2 == 0]

# print(squares)
# print(even_squares)
# ------------------------------------------------------------------------------------------------------------------------------


# # dictionary
# names = ["Alice", "Bob", "Charlie"]
# name_lengths = {name: len(name) for name in names}
# print(name_lengths)


# ------------------------------------------------------------------------------------------------------------------------------

# Given this list of temperatures in Celsius:

# celsius = [0, 10, 20, 30, 40]

# Create a new list of Fahrenheit temperatures using a list comprehension.
# Formula: F = C * 9/5 + 32
# Create a dictionary where the key is the Celsius value and the value is the Fahrenheit value.
# ------------------------------------------------------------------------------------------------------------------------------


# celsius = [0, 10, 660, 30, 40]

# # Create Fahrenheit list
# fahrenheit = [c * 9/5 + 32 for c in celsius]

# print("Fahrenheit:", fahrenheit)

# # Create Celsius -> Fahrenheit dictionary
# temperature_dict = {c: c * 9/5 + 32 for c in celsius}

# print("Dictionary:", temperature_dict)

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# from dotenv import load_dotenv
# import os

# load_dotenv()  # loads the .env file

# name = os.getenv("My_name")
# username = os.getenv("GitHub_name")

# print(f"Hello {name}, your GitHub is {username}")

# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------


# import requests
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def get_github_user(username: str) -> dict | None:
#     """Fetch public info of a GitHub user. Returns None if failed."""
#     url = f"https://api.github.com/users/{username}"
    
#     try:
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()  # raises error for 4xx/5xx
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print("API Error:", e)
#         return None

# # Usage
# user_data = get_github_user("sameer-tagde123")
# if user_data:
#     print("Name:", user_data.get("name"))
#     print("Repos:", user_data.get("public_repos"))
#     print("Bio:", user_data.get("bio"))




class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def is_adult(self) -> bool:
        return self.age >= 18


# Create objects
p1 = Person("Alex", 25)
p2 = Person("Sam", 16)

print(p1.greet())
print("Adult?" , p1.is_adult())
print(p2.greet())
print("Adult?" , p2.is_adult())