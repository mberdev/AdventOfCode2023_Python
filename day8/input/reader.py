"""docstring"""


def read_file(file_path, keep_empty_lines=False):
    """Reads a file and returns its contents as a list of lines."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    lines = [line.rstrip('\n') for line in lines]  # Strip newline character from each line
    
    if not keep_empty_lines:
        lines = [line for line in lines if line.strip() != ""]
    
    return lines
