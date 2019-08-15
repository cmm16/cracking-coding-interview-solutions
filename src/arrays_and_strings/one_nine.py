def is_substring(longer: str, shorter: str) -> bool:
    len_dif = len(longer) - len(shorter)
    for i in range(len_dif + 1):
        if longer[i:i + len(shorter)] == shorter:
            return True
    return False


def is_rotated(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False
    validation_string = string1 + string1
    return is_substring(validation_string, string2)
