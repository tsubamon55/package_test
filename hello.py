def hello():
    return "Hello"


class Hello(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello {self.name}"
