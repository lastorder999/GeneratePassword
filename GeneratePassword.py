import string
import secrets

def generate_password(length = 12):
    # characters = string.ascii_letters + string.digits + string.punctuation 
    characters = string.ascii_letters + string.digits
    secure_random = secrets.SystemRandom()
    password_list = [secure_random.choice(characters) for _ in range(length)]
    password_list.insert(4,"-")
    password_list.insert(9,"-")
    password = ''.join(password_list)
    print(password)
    

if __name__ == '__main__':
    number = int(input())
    for _ in range(number):
        generate_password()

