"""Password length"""

PASSWORD_LENGTH = 8

password = input("Password: ")

while len(password) < PASSWORD_LENGTH:
    print("Password not long enough.")
    password = input("Password: ")

print(len(password) * "*")
