my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict_copy = my_dict.copy()  
my_dict_copy.clear()
my_dict_copy = my_dict.copy()

keys = ['a', 'b', 'c']
new_dict = dict.fromkeys(keys, 0)


value = my_dict.get('name')
value_missing = my_dict.get('country', 'Not Found')

my_dict.items()
my_dict.keys()
my_dict.values()

removed_value = my_dict.pop('age')
removed_item = my_dict.popitem()
value_set = my_dict.setdefault('city', 'Unknown')
value_new = my_dict.setdefault('country', 'USA')
new_data = {'age': 30, 'profession': 'Engineer'}
my_dict.update(new_data)
my_dict
my_dict.values()

del my_dict['age']  
my_dict.clear()  
new_dict = dict.fromkeys(['x', 'y', 'z'], 0)  
my_dict = dict(a=1, b=2, c=3)  

for key, value in my_dict.items():
    print(f'{key}: {value}')
