class ColorFormat:
    def __init__(self):
        pass

    def red(self, text):
        return f"\033[91m{text}\033[00m"

    def green(self, text):
        return f"\033[92m{text}\033[00m"
