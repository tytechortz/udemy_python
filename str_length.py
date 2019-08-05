def string_length(word):
    if type(word) == int or type(word) == float:
        return "Sorry integers don't have length"
    else:
        return len(word)

print(string_length(10))