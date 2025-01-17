def find_non_repeating_elements(arr):
    count = {}
    for num in arr:
        count[num] = count.get(num, 0) + 1
    return [key for key, value in count.items() if value == 1]
arr = [4, 5, 6, 7, 4, 6, 8]
non_repeating = find_non_repeating_elements(arr)
print(non_repeating)
