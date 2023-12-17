"""docstring"""

import math
import os
from input.parser import split_into_groups
from input.reader import read_file
from input.parser import parse_line
from model import Node, OptimizedNode


def get_left_optimized(node: OptimizedNode) -> OptimizedNode:
    """Returns the left direction of the given node."""
    return node.directions[0]


def get_right_optimized(node: OptimizedNode) -> OptimizedNode:
    """Returns the right direction of the given node."""
    return node.directions[1]


def follow_directions_optimized(directions: [int], start_node: OptimizedNode):
    """Follows the given directions using the provided nodes."""
    directions_cursor: int = 0
    directions_length: int = len(directions)

    steps_count: int = 0

    direction_to_follow = directions[directions_cursor]
    current_node: OptimizedNode = start_node

    LOOP_LIMIT = 1000000

    while ((not current_node.is_end_label) and steps_count < LOOP_LIMIT):
        
        # Optional. For control.
        # print ("current_label: ", current_label)
        # print ("Going ", current_direction)

        if (direction_to_follow == 0):
            current_node = get_left_optimized(current_node)
        elif (direction_to_follow == 1):
            current_node = get_right_optimized(current_node)
        else:
            raise Exception("Invalid direction")
        

        # classic way of looping on a string
        directions_cursor = (directions_cursor+1)%directions_length

        # fetch next values
        direction_to_follow = directions[directions_cursor]

        steps_count += 1

        if (steps_count % 100000 == 0):
            print("steps_count: ", steps_count)
            # print("current_labels: ", current_labels)

    # print("current_labels: ", current_nodes)

    if (steps_count >= LOOP_LIMIT):
        raise Exception("Infinite loop detected")
    
    return steps_count



# Transforms the nodes to entirely remove the need for string
# parsing. Only references to other nodes.
def to_optimized(nodes: [Node]) -> [OptimizedNode]:
    """Converts the given nodes to OptimizedNode."""
    result: [OptimizedNode] = []
    
    # turn the structure into int-indexed array. Nodes not connected yet.
    for node in nodes:
        result.append(OptimizedNode(node.label, -1, [None, None]))
    
    for i in range(0, len(result) -1):
        result[i].label_hash = i
        
    # create links between nodes
    for node in nodes:
        optimized_node = find_node_by_label(result, node.label)

        label_left: int = node.directions[0]
        optimized_node.directions[0] = find_node_by_label(result, label_left)

        label_right: int = node.directions[1]
        optimized_node.directions[1] = find_node_by_label(result, label_right)
        
    return result

def find_node_by_label(nodes: [OptimizedNode], label: str) -> OptimizedNode:
    for n in nodes:
        if n.label == label:
            return n
    raise Exception("Node not found")


def to_optimized_directions(directions: str) -> [int]:
    """Converts the given directions string to an array of integers."""
    return [0 if direction == 'L' else 1 for direction in directions]


def main():
    """docstring"""
    # file_name:str = "./input/sample1.txt"
    # file_name:str = "./input/sample2.txt"
    # file_name:str = "./input/sample3.txt"
    file_name:str = "./input/data.txt"

    raw_lines = read_input(file_name)
    
    # Optional (For control)
    # for line in raw_lines:
    #     print(line)

    # parse input into model
    grouped: [[str]] = split_into_groups(raw_lines)
    directions: str = grouped[0][0] # first line of first group
    nodes_definitions: [str] = grouped[1] # all lines of second group
    nodes_list = [parse_line(node_direction) for node_direction in nodes_definitions]  # Call parse on each node_direction in nodes_directions

    # optimization not realy needed; that was before
    # I knew if the computations for part 2 would be heavy
    optimized_nodes = to_optimized(nodes_list)
    optimized_directions = to_optimized_directions(directions)

    # do "part 2"
    start_nodes: [OptimizedNode] = [n for n in optimized_nodes if n.label[-1] == 'A']
    loop_lengths:[int] = []
    for n in start_nodes:
        count: int = follow_directions_optimized(optimized_directions, n)
        print(f"loop when starting from {n.label}: {count}")
        loop_lengths.append(count)

    smallest_multiple = math.lcm(*loop_lengths)
    print("Smallest multiple:", smallest_multiple)


def read_input(file_name):

    # Get the current execution path
    current_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_path, file_name)
    
    raw_lines = read_file(file_path, keep_empty_lines=True)
    return raw_lines

if __name__ == "__main__":
    main()
