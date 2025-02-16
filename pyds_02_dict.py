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

my_dict.pop('age')
my_dict.popitem()
my_dict.setdefault('city', 'Unknown')
my_dict.setdefault('country', 'USA')


# list extend is same as dict.updated
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


from sklearn.datasets import load_iris
import pandas as pd


def create_iris_dataframe():
    iris = load_iris()

    iris_dict = {}
    features_dict = {}

    for feature in iris.feature_names:
        f_str = feature.replace(" ", "_")
        f_str = f_str.replace("_(cm)","")
        features_dict[f_str] = iris.data[:, i]

    target_dict = {}
    target_names = iris.target_names
    lab = 0 
    for name in target_names:
        new_label = "is_" + name
        target_dict[new_label] = (iris.target==lab)*1
        lab += 1

    target_dict   

    iris_dict
    iris_dict.update(features_dict)
    iris_dict.update(target_dict)

    df = pd.DataFrame(iris_dict)

    return df
