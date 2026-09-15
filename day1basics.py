
# name = "Alex"          # string
# age = 25               # integer
# height = 1.75          # float
# is_learning = True     # boolean

# print("Hello,", name)
# print(f"I am {age} years old and {height}m tall.")  # f-string (modern way)
# print(type(name), type(age), type(is_learning))


# name=  input("enter your name: ")
# age= int (input("enter your age: "))
# print("enter your name ", name)

# if age >=18 :{
#      print("age is greater than 18")
# }
# else:{
#     print("below age")
# }


# ------------------------------------------------------------------------------------------------------------------------------

  # List
# skills = ["Python", "Git", "APIs"]
# skills.append("FastAPI")
# print(skills[0])        # first item
# print(len(skills))

# # Dictionary (very important for JSON later)
# person = {
#     "name": "Alex",
#     "age": 25,
#     "skills": ["Python", "Git"]
# }
# print(person["name"])
# print(person.get("city", "Not specified"))  # safe way

# import json

# data = {
#     "name": "Alex",
#     "goals": ["Learn Python", "Build RAG", "Get a GenAI job"]
# }

# # Save to file
# with open("my_data.json", "w") as f:
#     json.dump(data, f, indent=2)

# # Read from file
# with open("my_data.json", "r") as f:
#     loaded = json.load(f)

# print(loaded)

# import json
# data1 = {
# "name":"sameer",
# "goal": ["Learn Python", "Fast API","Build Model", "become Genai Dev"]
# }

# with open("day1_goals.json", "w") as f:
#     json.dump(data1, f, indent=2)



# with open("day1_goals.json", "r") as f:
#     load=json.load(f)
#     print(data1["goal"])

# ------------------------------------------------------------------------------------------------------------------------------



import string

import requests

response = requests.get("https://api.github.com/users/sameer")


if response.status_code == 200:
    user = response.json()
    print("Name:", user["name"])
    print("Public repos:", user["public_repos"])
    print("Bio:", user.get("bio"))
else:
    print("Error:", response.status_code  )       