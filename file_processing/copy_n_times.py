with open("data.txt" "a+") as file:
    file.seek(0)
    content = file.read()
    print(content)
    file.seek(0)
    file.write(content)
    file.write(content)