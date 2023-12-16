"""docstring"""

import os
from input.parser import split_into_groups
from input.reader import read_file
from input.parser import parse_line
from model import Node


def get_left(node: Node) -> str:
    """Returns the left direction of the given node."""
    return node.directions[0]

def get_right(node: Node) -> str:
    """Returns the right direction of the given node."""
    return node.directions[1]

def follow_directions_part1(directions: str, nodes: dict[str, Node]):
    """Follows the given directions using the provided nodes."""
    directions_cursor: int = 0
    directions_length: int = len(directions)

    steps_count: int = 0

    current_label: str = "AAA"
    current_direction = directions[directions_cursor]
    current_node = nodes[current_label]

    while current_label != "ZZZ" and steps_count < 100000:
        
        # Optional. For control.
        # print ("current_label: ", current_label)
        # print ("Going ", current_direction)

        if (current_direction == 'L'):
            current_label = get_left(current_node)
        elif (current_direction == 'R'):
            current_label = get_right(current_node)
        else:
            raise Exception("Invalid direction")
        

        # classic way of looping on a string
        directions_cursor = (directions_cursor+1)%directions_length

        # fetch next values
        current_direction = directions[directions_cursor]
        current_node = nodes[current_label]

        steps_count += 1

    if (steps_count >= 100000):
        raise Exception("Infinite loop detected")
    
    return steps_count


def all_end_in_Z(strings: list[str]) -> bool:
    """Returns True if the last letter of all strings is 'Z', False otherwise."""
    for string in strings:
        if string[-1] != 'Z':
            return False
    return True

def follow_directions_part2(directions: str, nodes: dict[str, Node]):
    """Follows the given directions using the provided nodes."""
    directions_cursor: int = 0
    directions_length: int = len(directions)

    steps_count: int = 0

    # start with all the labels ending in 'A'
    current_labels = [k for k in nodes.keys() if k[-1] == 'A']

    current_direction = directions[directions_cursor]
    current_nodes = get_nodes_by_labels(current_labels, nodes)

    while ((not all_end_in_Z(current_labels)) and steps_count < 10000000):
        
        # Optional. For control.
        # print ("current_label: ", current_label)
        # print ("Going ", current_direction)

        if (current_direction == 'L'):
            current_labels = [get_left(node) for node in current_nodes]
        elif (current_direction == 'R'):
            current_labels = [get_right(node) for node in current_nodes]
        else:
            raise Exception("Invalid direction")
        

        # classic way of looping on a string
        directions_cursor = (directions_cursor+1)%directions_length

        # fetch next values
        current_direction = directions[directions_cursor]
        current_nodes = get_nodes_by_labels(current_labels, nodes)

        steps_count += 1

        if (steps_count % 1000 == 0):
            print("steps_count: ", steps_count)
            # print("current_labels: ", current_labels)

    print("current_labels: ", current_labels)

    if (steps_count >= 10000000):
        raise Exception("Infinite loop detected")
    
    return steps_count

def get_nodes_by_labels(labels, nodes):
    return [nodes[key] for key in nodes.keys() if key in labels]




def main():
    """docstring"""
    # file_name:str = "./input/sample1.txt"
    # file_name:str = "./input/sample2.txt"
    # file_name:str = "./input/sample3.txt"
    file_name:str = "./input/data.txt"

    raw_lines = read_input(file_name)
    
    # Optional (For control)
    for line in raw_lines:
        print(line)

    # parse input into model
    grouped: list[list[str]] = split_into_groups(raw_lines)
    directions: str = grouped[0][0]
    nodes_definitions: list[str] = grouped[1]
    nodes_list = [parse_line(node_direction) for node_direction in nodes_definitions]  # Call parse on each node_direction in nodes_directions
    nodes_dict: dict[str,Node] = {node.label: node for node in nodes_list}  # Convert list to dict for "quick" (Python, lol) search
    
    
    # do "part 1" of the exercise
    count: int = follow_directions_part2(directions, nodes_dict)
    print("Steps count: ", count)
    
     

def read_input(file_name):

    # Get the current execution path
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, file_name)
    
    raw_lines = read_file(file_path, keep_empty_lines=True)
    return raw_lines

if __name__ == "__main__":
    main()
