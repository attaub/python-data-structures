my_list = [10, 20, 30, 40, 50]
my_list.append(60)

my_list.copy()  
my_list_copy.clear()
my_list.count(20)
my_list.extend([70, 80, 90])
my_list.index(30)
my_list.insert(3, 25)  
my_list.pop()  
my_list.pop(2)  # Remove the element at index 2
my_list.remove(40)  # Removes the first occurrence of 40
my_list.reverse()
my_list.sort()
list((1, 2, 3))  
my_list.extend(list(1,2,3))
my_list.append([100, 200, 300])
string_list = ['elephant', 'dog', 'cat', 'lion']
string_list.sort(key=len)  
sorted(my_list)

# list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
# newlist = [expression for item in iterable if condition == True]

