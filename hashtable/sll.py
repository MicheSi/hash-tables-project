class Node:
    def __init__(sefl, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def add_to_head(self, node):
        node.next = self.head
        self.head = node
        