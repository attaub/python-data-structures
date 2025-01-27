#######################
"""
A = set()
union()
intersection()
difference()
discard()
update()

"""
A = {"apple", "banana", "cherry"}
B = {"apple", "banana", "cherry", True, 1, 2}
C = {"apple", "banana", "cherry"}
A.add("orange")
A.update(B)
B.remove("banana")
A.discard("banana")
x = thisset.pop()
A.clear()
del A
D = A.union(B)
E = A | B
F = A.union(B, C, D)
G = A | B | C | D

y = (1, 2, 3)
Z = A.union(y)

A.update(B)

H = A.intersection(B)
M = A & B
A.intersection_update(B)
N = A.intersection(B)
M = A.difference(B)
O = A - B

A.difference_update(B)
P = A.symmetric_difference(B)
Q = A ^ B
A.symmetric_difference_update(B)
