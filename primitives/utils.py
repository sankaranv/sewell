class Node:

    def __init__(self, name, data=None):
        
        self.name = name
        self.data = data
        self.parents = set()
        self.children = set()
        self.neighbors = set()

    def is_root(self):
        return len(self.parents) == 0

    