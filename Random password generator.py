import random
import string
def generate_random_password(length):
    """Generates a secure, random password of a given length."""
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 1:
        return "The length of the password must be at least 1."
    password = ''.join(random.choices(all_characters, k=length))
    return password
try:
    length = int(input("Enter the length of password e.g., 12): "))
    secure_password = generate_random_password(length)
    print("\nGenerated Password:")
    print(secure_password)
except ValueError:
    print("\nError: Please enter a nummber as length")