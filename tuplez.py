mytuple = ("apple", "banana", "cherry")
("apple", "banana", "cherry") + ("orange",)


fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")


(green, *tropic, red) = fruits



tuple1 = (1, 2, 3, 4)
tuple2 = ("apple", 3.14, 10)
single_element_tuple = (42,)
empty_tuple = ()


# Using count() method
tuple3 = (1, 2, 2, 3, 4, 2)
count_of_2 = tuple3.count(2)


# Using index() method
index_of_3 = tuple3.index(3)

try:
    tuple3.index(5)
except ValueError as e:
    print("Error:", e)

# Iterating through tuple
print("Iterating through tuple3:")
for item in tuple3:
    print(item)



