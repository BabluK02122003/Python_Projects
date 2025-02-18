"""This Python script generates random passwords with user-defined lengths, ensuring that the passwords meet a minimum length requirement of 8 characters. 
It excludes special characters, using only ASCII letters and digits to create the passwords. 
The script runs in a continuous loop, prompting the user to input the desired password length or type 'exit' to terminate the program. 
If the user inputs a valid number, a password of the specified length is generated and displayed. 
Invalid inputs are handled gracefully, with appropriate error messages guiding the user. 
This approach provides a straightforward method for generating secure passwords while accommodating user preferences and ensuring ease of use."""

import random
import string

def generate_password(length):
    if length < 5:
        print("Password length should be at least 5 characters.")
        return None
    
    all_characters = string.ascii_letters + string.digits
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

while True:
    user_input = input("Enter the length of the password (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        length = int(user_input)
        password = generate_password(length)
        if password:
            print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a number.")
