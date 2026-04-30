class AsciiArt:
    def __init__(self, characters):
        self._characters = characters

    def __str__(self):
        return self._characters

    @classmethod
    def from_file(cls, file_path):
        with open(file_path) as f:
            return cls(f.read())

if __name__ == '__main__':
    ascii_art = AsciiArt.from_file("./face.txt")
    print(ascii_art)