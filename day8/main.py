"""docstring"""

import os
from input_utils import read_file


def main():
    """docstring"""
    file_name:str = "./input/sample.txt"

    # Get the current execution path
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, file_name)
    
    lines = read_file(file_path, keep_empty_lines=True)
    
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
    

if __name__ == "__main__":
    main()
