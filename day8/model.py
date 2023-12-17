class Node:
    """doctstring"""
    def __init__(self, label, directions: [str]):
        self.label = label
        self.directions = directions

    
class OptimizedNode:
    """doctstring"""
    def __init__(self, label: str, label_hash: int, directions: []):
        self.label = label
        self.label_hash = label_hash
        self.directions = directions
        self.is_end_label: bool = label[-1] == 'Z'

    
    