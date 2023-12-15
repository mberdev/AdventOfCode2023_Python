"""docstring"""

def read_file(file_path):
    """docstring"""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines
