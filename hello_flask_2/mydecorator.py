def make_bold(function):
    def wrapper_function():
        text = "<b>"
        text += function()
        text += "</b>"
        return text

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        text = "<em>"
        text += function()
        text += "</em>"
        return text

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        text = "<u>"
        text += function()
        text += "</u>"
        return text

    return wrapper_function
