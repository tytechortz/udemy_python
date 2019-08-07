def foo(character,filepath="bear.txt"):
    myfile = open(filepath)
    content = myfile.read()
    return content.count(character)