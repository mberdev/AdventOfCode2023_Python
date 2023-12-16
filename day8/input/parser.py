from typing import List

from model import Node

def split_into_groups(strings):
    """Groups strings together"""
    # (A group is defined as: separated by one or more blank lines)
    groups = []
    current_group = []

    for string in strings:
        if string.strip() == "":
            if current_group:
                groups.append(current_group)
                current_group = []
        else:
            current_group.append(string)

    if current_group:
        groups.append(current_group)

    return groups


def parse_line(string):
    """AAA = (BBB, CCC) -> {'label': 'AAA', 'directions': ['BBB', 'CCC']}"""
    parts: List[str] = string.split('=', 1)
    label: str = parts[0].strip()
    directions_raw: str = parts[1]
    directions: list[str] = directions_raw.strip().replace(' ', '').replace('(', '').replace(')', '').split(',')
    result: Node = Node(label, directions)
    return result
