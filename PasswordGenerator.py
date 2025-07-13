import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be greater than 0")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except:
        print("Invalid input")

main()
