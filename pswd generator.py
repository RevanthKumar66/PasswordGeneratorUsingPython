import string
import random

# User Input: Prompt the user to specify the desired length of the password.
print("Welcome to the password generator!")
print("Please enter the length of the password you want to generate.")
length = int(input("Length: "))

# Generate Password: Use a combination of random characters to generate a password of the specified length.
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_characters) for i in range(length))

# Display the Password: Print the generated password on the screen.
print("Here is your generated password:")
print(password)