import string
import random

class PasswordGenerator:
    def __init__(self, length=12, use_symbols=True, use_numbers=True):
        self.length = length
        self.use_symbols = use_symbols
        self.use_numbers = use_numbers

    def generate_password(self):
        characters = string.ascii_letters
       # print(characters)
        if self.use_symbols:
            characters += string.punctuation
           # print(characters)
        if self.use_numbers:
            characters += string.digits
            #print(characters)

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

class FileHandler:
    def save_password(self, filename, password):
        with open(filename, 'w') as file:
            file.write(password)

    def read_password(self, filename):
        with open(filename, 'r') as file:
            return file.read()

# Example usage
generator = PasswordGenerator(length=101, use_symbols=True)
password = generator.generate_password()

file_handler = FileHandler()
file_handler.save_password('mypassword.txt', password)

# To read the password back
saved_password = file_handler.read_password('mypassword.txt')
print("Generated Password:", password)
print("Saved Password:", saved_password)
