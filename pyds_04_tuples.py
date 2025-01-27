tup1 = ("apple", "banana", "cherry")
tup2 = ("apple", "banana", "cherry") + ("orange",)

tup = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = tup
(green, *tropic, red) = tup

single_tup = (42,)
empty_tup = ()


tup = (1, 2, 2, 3, 4, 2)
count_of_2 = tup.count(2)
index_of_3 = tup.index(3)
