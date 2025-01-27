from collections import deque

class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack

############################################

stack_list = StackUsingList()
stack_list.push(10)
stack_list.push(20)
stack_list.push(30)

stack_list.display()
stack_list.pop()
stack_list.display()
stack_list.peek()
stack_list.is_empty()


##################################################################

class StackUsingDeque:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        return list(self.stack)
############################################
stack_deque = StackUsingDeque()
stack_deque.push(10)
stack_deque.push(20)
stack_deque.push(30)

stack_deque.display()
stack_deque.pop()
stack_deque.display()
stack_deque.peek()
stack_deque.is_empty()

############################################
"""
https://docs.python.org/3/library/collections.html
dequer: list-like container with fast appends and pops on either end

deque methods: 
append()
appendleft()
clear()
copy()
count()
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

d.append(6)
d.appendleft(0)
d.clear()
d = deque([1, 2, 3])
d_copy = d.copy()
d = deque([1, 2, 3, 1, 4, 1])
d.count(1)
d = deque([1, 2])

d.extend([3, 4, 5])
d.extendleft([1, 2])
d = deque([1, 2, 3, 4, 2])
d.index(2)  

d = deque([1, 2, 3])
d.insert(1, 1.5) 

d = deque([1, 2, 3])
d.pop()  

d = deque([1, 2, 3])
d.popleft()  

d = deque([1, 2, 3, 4, 3])
d.remove(3) 

d = deque([1, 2, 3, 4])
d.reverse() 

d = deque([1, 2, 3, 4])
d.rotate(1) 

d.rotate(-2) 

d = deque([1, 2, 3], maxlen=3)
d.append(4) 
