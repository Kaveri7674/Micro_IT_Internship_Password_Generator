import random
import string
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 for good security."
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Input from user
try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
