"""
A stack is a linear data structure that follows LIFO principle.
Last element added to the stack will be the first one to be removed.

Stack in Python can be implemented using a list,
or collections.deque class for more efficient operations. 

"""
# collections implements datatypes alternative to dict, list, set, tuple

"""
https://docs.python.org/3/library/collections.html

namedtuple(): create tuple subclasses with named fields
dequer: list-like container with fast appends and pops on either end
ChainMap: dict-like class for creating a single view of multiple mappings
Counter: dict subclass for counting hashable objects
OrderedDict: dict subclass that remembers the order entries were added
defaultdict: dict subclass that calls a factory function to supply missing values
UserDict: wrapper around dictionary objects for easier dict subclassing
UserList: wrapper around list objects for easier list subclassing
UserString: wrapper around string objects for easier string subclassing
"""

"""
deque methods: 
append(x)
appendleft(x)
clear()
copy()
count(x)
extend(iterable)
extendleft(iterable)
index(x[, start[, stop]])
insert(i, x)
pop()
popleft()
remove(value)
reverse()
rotate(n=1)
maxlen
"""

# deque
from collections import deque
d = deque()
d = deque([1, 2, 3, 4, 5])

# append
d.append(6)
d.appendleft(0)
d.clear()
d = deque([1, 2, 3])
d_copy = d.copy()
d = deque([1, 2, 3, 1, 4, 1])
d.count(1)
d = deque([1, 2])

d.extend([3, 4, 5])
d = deque([3, 4, 5])
d.extendleft([1, 2])
d = deque([1, 2, 3, 4, 2])
d.index(2)  # 1

d = deque([1, 2, 3])
d.insert(1, 1.5) # deque([1, 1.5, 2, 3])

d = deque([1, 2, 3])
d.pop()  # 3, deque([1, 2])

d = deque([1, 2, 3])
d.popleft()  # 1, deque([2, 3])

d = deque([1, 2, 3, 4, 3])
d.remove(3) # deque([1, 2, 4, 3])

d = deque([1, 2, 3, 4])
d.reverse() # deque([4, 3, 2, 1])

d = deque([1, 2, 3, 4])
d.rotate(1) # deque([4, 1, 2, 3])

d.rotate(-2) # deque([2, 3, 4, 1])

d = deque([1, 2, 3], maxlen=3)
d.append(4) # deque([2, 3, 4]),  1 is removed, as maxlen is 3


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

