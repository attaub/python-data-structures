############################################
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        # create a new node
        new_node = Node(val)

        # check if the list is empty
        if self.head is None:
            self.head = new_node
            return

        # Starts at the head and iterates through the list to find the last node
        last = self.head
        print("Current Value:", val, "head:", self.head.val)

        while last.next:
            last = last.next
            print("last.next", last.next)
            print("last.val", last.val)

        last.next = new_node
        print("last.next.val", last.next.val)
        print("last.next.val", last.next.next)

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def delete_node(self, key):
        current = self.head
        if current and current.val == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.val != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.val == key:
                return True
            current = current.next
        return False


# Example usage:
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)

print("Linked List:")
llist.print_list()  # Output: 10 -> 20 -> 30 -> 40 -> None

# Search for a value
print("Is 20 in the list?", llist.search(20))  # Output: True
print("Is 50 in the list?", llist.search(50))  # Output: False

# Delete a node
llist.delete_node(20)
print("Linked List after deleting 20:")
llist.print_list()  # Output: 10 -> 30 -> 40 -> None
