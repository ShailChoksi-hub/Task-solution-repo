def count_occurrences(input_string, target_character):
    count = 0
    for char in input_string:
        if char == target_character:
            count += 1
    return count


input_string1 = "geeksforgeeks"
target_character1 = 'e'
result1 = count_occurrences(input_string1, target_character1)
print(f"Count of '{target_character1}' in '{input_string1}': {result1}")

input_string2 = "abccdefgaa"
target_character2 = 'a'
result2 = count_occurrences(input_string2, target_character2)
print(f"Count of '{target_character2}' in '{input_string2}': {result2}")
