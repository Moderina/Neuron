class Cprint:
    def __init__(self, console) -> None:
        self.console = console

    def print(self, text):
        self.console.insert("1.0", text)