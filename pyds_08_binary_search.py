""" 
Given a sorted array of integers nums (in ascending order) and an integer tar
get. Write a function to find the index of target in nums. If the target is n
ot present, return -1.
"""


class BinarySearch:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def iterative_search(self):
        # Iterative binary search
        left = 0
        right = len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == self.target:
                return mid
            elif self.arr[mid] < self.target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def recursive_search(self, arr, target, left, right):
        # Base case
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return self.recursive_search(arr, target, left, mid - 1)

        else:
            return self.recursive_search(arr, target, mid + 1, right)


############################################
# use case
arr = [-10, -5, 0, 3, 7, 10, 15]
target = 3
binary_search = BinarySearch(arr, target)

# Iterative search
result_iterative = binary_search.iterative_search()
print(f"Target found at index (iterative): {result_iterative}")  #Output: 3

# Recursive search
result_recursive = binary_search.recursive_search(arr, target, 0, len(arr) - 1)
print(f"Target found at index (recursive): {result_recursive}")  #Output: 3
