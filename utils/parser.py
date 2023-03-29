def parse_list(test_case_path: str, separator=" ", to_int=False):
    # read mode ("r") is by default
    with open(test_case_path, "r") as file:
        list_string = file.read().strip()
        parsed_list = list_string.split(separator)
    if to_int:
        parsed_list = list(map(int, parsed_list))

    return parsed_list
