# Given sorted array and a target
# find the index of target in nums.
# return -1 otherwise.


def iterative_binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2

        if arr[m] == target:
            return m

        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1


def recursive_binary_search(arr, target, l, r):
    if l > r:
        return -1

    mid = (l + r) // 2

    if arr[m] == target:
        return m

    elif arr[m] > target:
        return recursive_binary_search(arr, target, l, mid - 1)

    else:
        return recursive_binary_search(arr, target, mid + 1, r)


arr = [-10, -5, 0, 3, 7, 10, 15]
target = 3

result_iterative = iterative_binary_search()
result_recursive = recursive_binary_search(arr, target, 0, len(arr) - 1)
