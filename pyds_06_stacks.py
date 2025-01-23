"""
A stack is a linear data structure that follows LIFO principle.
Last element added to the stack will be the first one to be removed.

Stack in Python can be implemented using a list,
or collections.deque class for more efficient operations. 

"""
# Stack using Python List
class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack. Return None if stack is empty."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Return the top element without removing it. Return None if stack is empty."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def display(self):
        """Display all elements in the stack."""
        return self.stack


# Example Usage
stack_list = StackUsingList()
stack_list.push(10)
stack_list.push(20)
stack_list.push(30)

print("Stack (List) after pushing elements:", stack_list.display())
print("Popped element:", stack_list.pop())
print("Stack (List) after popping an element:", stack_list.display())
print("Top element:", stack_list.peek())
print("Is stack empty?", stack_list.is_empty())


# Stack using deque

from collections import deque
class StackUsingDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        """Push an item onto the stack."""
        self.stack.append(item)

    def pop(self):
        """Pop an item from the stack. Return None if stack is empty."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        """Return the top element without removing it. Return None if stack is empty."""
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self.stack)

    def display(self):
        """Display all elements in the stack."""
        return list(self.stack)


# Example Usage
stack_deque = StackUsingDeque()
stack_deque.push(10)
stack_deque.push(20)
stack_deque.push(30)

print("Stack (Deque) after pushing elements:", stack_deque.display())
print("Popped element:", stack_deque.pop())
print("Stack (Deque) after popping an element:", stack_deque.display())
print("Top element:", stack_deque.peek())
print("Is stack empty?", stack_deque.is_empty())

