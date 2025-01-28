string = input()
character = "!@#$%^&*()_+-=[]<>,.?/@"
updatedstring = ""
for char in string:
    if char in character:
        continue
    else:
        updatedstring = updatedstring+char
print(updatedstring)
