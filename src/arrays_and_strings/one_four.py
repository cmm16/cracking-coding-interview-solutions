from collections import defaultdict

# needs work
def palindrome_permutations(string: str) -> (bool, str):
    char_count_map = defaultdict(int)
    for char in string:
        char_count_map[char] += 1

    for key, num in char_count_map.items():
        if num % 2 == 1:
            pass

