import random
import string

class InvalidPasswordLengthError(Exception):
    def __init__(self, message):
        self.message = message
        

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(characters,k=length))
    return password
try:
    length = int(input("Enter the length of the password (Min 5 characters):"))
    if length < 5:
        raise InvalidPasswordLengthError("Error: Password length must be a positive integer greater than 5")
    else:
        print(f"Generated Password : {generate_password(length)}")    
   
except ValueError:
    print("Error:ENTER A VALID INPUT")
except InvalidPasswordLengthError as e:
    print(e)

