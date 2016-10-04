class Typing(object):
    def __init__(self):
        self.typing_register = {}

    def register_type(self, name, parse_function):
        self.typing_register[name] = parse_function
        # register_type(name, parse_function)

    def __str__(self):
        return ",".join(self.typing_register.keys())
