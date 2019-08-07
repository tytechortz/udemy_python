fruitsfile = open("fruits.txt")
content = fruitsfile.read()
fruitsfile.close()
content = content.splitlines()
for fruit in content:
    print(len(fruit))
