from collections import defaultdict


def is_unique(string: str) -> bool:
    char_map = defaultdict(bool)
    for char in string:
        if char_map[char]:
            return False
        else:
            char_map[char] = True
    return True


