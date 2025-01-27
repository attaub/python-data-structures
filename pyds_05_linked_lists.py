#####################
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#####################
class LinkedList:
    def __init__(self):
        self.head = None

    def update(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            # print(current.val, end=" -> ")
            print(current.val, end=" ---> ")
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


#################
val_arr = [10, 20, 40, 80, 160]
ll = LinkedList()

print(val_arr)

for i in range(len(val_arr)):
    ll.update(i)
    ll.print_list()

#################
ll.search(20)
ll.search(50)

#################
ll.delete_node(20)
ll.print_list()
