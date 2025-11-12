"""
Task 3
Have the user enter in the following information and 
store it into a dictionary.  Use an appropriate key 
for each element of the dictionary.

first name
last name
student number
birthdate
grade
email

Then create a loop to repeatedly ask the user for a key.
If the key is in the dictionary, display the value.
If the user types in "quit" then stop the loop.
"""
def create():
    student = {}
    student["first name"] = input("Enter first name: ")
    student["last name"] = input("Enter last name: ")
    student["student number"] = input("Enter student number: ")
    student["birthdate"] = input("Enter birthdate: ")
    student["grade"] = input("Enter grade: ")
    student["email"] = input("Enter email: ")
def loop(information):
    
    s = input("what would you like to know?: ")
    if s in information: 
        print(information[s])
    elif s == "Quit" or s == "quit":
        break
    else:
        print("We do not store that information")

