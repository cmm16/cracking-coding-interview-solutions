def one_edit_away(string_a: str, string_b: str) -> bool:
    len_a = len(string_a)
    len_b = len(string_b)

    if len_a == len_b:
        return is_replace(string_a, string_b)
    elif len_a - len_b == 1:
        return is_other_edit(string_a, string_b)
    elif len_b - len_a == 1:
        return is_other_edit(string_b, string_a)
    else:
        return False


def is_replace(string_a: str, string_b: str) -> bool:
    single_replace: bool = False
    for i, char in enumerate(string_a):
        if char != string_b[i]:
            if single_replace:
                return False
            single_replace = True
    return True if single_replace else False


def is_other_edit(longer: str, shorter: str) -> bool:
    single_edit: bool = False

    for i, char in enumerate(shorter):
        if not single_edit:
            if char != longer[i]:
                if char == longer[i + 1]:
                    single_edit = True
                else:
                    return False
        else:
            if char != longer[i + 1]:
                return False

    return True



