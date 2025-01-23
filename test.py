class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.val
        print("None")

    def delete_node(self, key):
        current = self.head

        if current and current.val == key:
            self.head = current.next
            current = None
            return
        prev = None

        while current and current.val == key:
            prev = curret
            current = current.next

        if current is None:
            return
        prev.next = current.next

        current = None


############################################
