correct_password = "python123"
name = input("Enter name: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password. Enter password again: ")

print("Hi, {}, You are logged in".format(name))