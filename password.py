import random
import string

def generate_password(length=12):
    if length < 1:
        return "Password length must be at least 1."
    
    # Combine uppercase and lowercase letters
    characters = string.ascii_letters  # Includes both uppercase and lowercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 12  # You can change the length as needed
print("Generated Password:", generate_password(password_length))
