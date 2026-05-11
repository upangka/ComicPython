"""
Hello World
"""
def print_working_dir():
    import os
    print(os.getcwd())
    print(__file__)

    from pathlib import Path
    print(Path("fear.txt").resolve())

print(__doc__)
if __name__ == '__main__':
    print_working_dir()