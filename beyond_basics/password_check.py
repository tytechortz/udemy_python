correct_password = "python123"
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password. Enter password again: ")

print("Logged in")