def string_compression(string: str) -> str:
    if string != "":
        new_string: str = string[0]
    else:
        return ""

    char_count = 1
    for i in range(1, len(string)):
        current_char = string[i]
        last_char = string[i - 1]
        if current_char == last_char:
            char_count += 1
        else:
            new_string += str(char_count) + current_char
            char_count = 1
    new_string += str(char_count)

    return new_string if len(new_string) < len(string) else string


print(string_compression("abbaaaaaAAAAaaaaceedef"))