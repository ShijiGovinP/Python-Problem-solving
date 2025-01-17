def find_repeated_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return {char: count for char, count in char_count.items() if count > 1}
string = "programming"
repeated_chars = find_repeated_characters(string)
print(repeated_chars)  
