def find_(s):
    length = len(s)
    middle = length // 2 
    if length % 2 == 0:  
        return s[middle - 1:middle + 1]
    else:  
        return s[middle]
string1 = "hello"
string2 = "python"
print("Middle character(s) of " + string1 + "':", find_middle_character(string1))
print("Middle character(s) of " + string2 + "':", find_middle_character(string2))
