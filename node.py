class Node:
    num_of_nodes = 0

    def __init__(self, value):
        self.value = value
        self.next = None
        Node.num_of_nodes += 1
