import sys

variable = sys.stdin.readline().strip()
uppers = {x: 1 for x in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def is_camel_form(var):
    if var[0] in uppers:
        return False

    if var.find("_") != -1:
        return False

    result = False
    for c in list(var):
        if c in uppers:
            result = True
            break

    return result


def is_snake_form(var):
    if var.find("_") == -1:
        for c in list(var):
            if c in uppers:
                return False
    elif var.find("_") == 0:
        return False
    else:
        words = var.split("_")
        for word in words:
            if len(word) < 1:
                return False

        for c in list(var):
            if c in uppers:
                return False

    return True


def convert_variable_name(var):
    camel = is_camel_form(var)
    snake = is_snake_form(var)
    if snake:
        result = convert_snake_to_camel(var)
    elif camel:
        result = convert_camel_to_snake(var)
    else:
        result = 'Error!'
    return result


def convert_snake_to_camel(var):
    words = var.split("_")
    to_upper = list(map(lambda x: x[0].upper() + x[1:], words[1:]))
    return "".join([words[0]] + to_upper)


def convert_camel_to_snake(var):
    words = []
    start = 0
    for i, c in enumerate(list(var)):
        if c in uppers:
            words.append(var[start:i])
            start = i

    words.append(var[start:])
    to_snake = list(map(lambda x: '_' + x[0].lower() + x[1:], words[1:]))
    return "".join([words[0]] + to_snake)


print(convert_variable_name(variable))
