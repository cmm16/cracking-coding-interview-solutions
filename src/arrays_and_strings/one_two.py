from collections import defaultdict


# not best run time currently a
def is_substring(string_a: str, string_b: str) -> bool:
    smaller_string, smaller_string_len, larger_string = (string_a, len(string_a), string_b) \
        if len(string_a) <= len(string_b) else (string_b, len(string_b), string_a)

    sm_str_map = defaultdict(int)
    for char in smaller_string:
        sm_str_map[char] += 1

    for i, char in enumerate(larger_string):
        chars_left = smaller_string_len
        for j in range(smaller_string_len):
            if sm_str_map[char] != 0:
                sm_str_map[char] -= 1
                chars_left -= 1
        if chars_left == 0:
            return True

    return False




