from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def add_first(self, value):
        node = Node(value)
        next_node = self.head
        self.head = node
        self.head.next = next_node
        self.num_of_nodes += 1

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.num_of_nodes += 1

    def remove(self, value):
        current_node = self.head
        if current_node.value == value:
            self.head = current_node.next
            self.num_of_nodes -= 1
            return
        else:
            while current_node.next is not None:
                if current_node.next.value == value:
                    next_node = current_node.next.next
                    current_node.next = next_node
                    self.num_of_nodes -= 1
                else:
                    current_node = current_node.next

    def clear(self):
        self.head = None

    def is_exist(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next
        return False

    def to_array(self):
        current_node = self.head
        arr = []
        while current_node is not None:
            arr.append(current_node.value)
            current_node = current_node.next
        return arr

    def length(self):
        if self.head is not None:
            return self.num_of_nodes
        else:
            return 0

    def print_linked_list(self):
        if self.head is not None:
            current_node = self.head
            print('[', end='')
            while current_node is not None:
                print(current_node.value, ', ', end='')
                current_node = current_node.next
            print(']', end='')

