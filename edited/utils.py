def handle_input(s: list[str]):
    line_num = -1
    def increment():
        nonlocal line_num
        line_num += 1
        if line_num < len(s):
            return s[line_num].replace("\n", "")
        raise IndexError("Index out of Bounds")
    return increment