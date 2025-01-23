my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.clear()
my_set = {1, 2, 3, 4, 5}
set_copy = my_set.copy()
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_result = set1.difference(set2)

# Shortcut: -=
set1.difference_update(set2)

set1.discard(3)  # 3 is not in set1, no error raised

# Shortcut: &
intersection_result = set1.intersection(set2)

# Shortcut: &=
set1.intersection_update(set2)

is_disjoint_result = set1.isdisjoint(set2)

# Shortcut: <=
is_subset_result = set1.issubset(set2)

# Shortcut: >=
is_superset_result = set2.issuperset(set1)

popped_element = set2.pop()

set2.remove(5)

# Shortcut: ^
symmetric_diff_result = set1.symmetric_difference(set2)

# Shortcut: ^=
set1.symmetric_difference_update(set2)

# Shortcut: |
union_result = set1.union(set2)
set1.update([7, 8])
