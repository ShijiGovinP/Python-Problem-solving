def find_middle_character(s):
    length = len(s)
    middle = length // 2  # Calculate the middle index
    
    if length % 2 == 0:  # If the length is even
        return s[middle - 1:middle + 1]
    else:  # If the length is odd
        return s[middle]

# Example usage
string1 = "hello"
string2 = "python"

print(f"Middle character(s) of '{string1}': {find_middle_character(string1)}")
print(f"Middle character(s) of '{string2}': {find_middle_character(string2)}")
