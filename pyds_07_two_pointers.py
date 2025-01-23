## process data from both ends towards center (or from center towards ends)
# efficient way to reduce time complexity
# Finding if a list has two numbers that sum up to a given target


def two_sum(nums, target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    # Loop until the two pointers meet
    while left < right:
        current_sum = nums[left] + nums[right]

        # Check if found the pair
        if current_sum == target:
            return [nums[left], nums[right]]  # Return the pair

        # If sum small, move left pointer to right
        elif current_sum < target:
            left += 1

        # If sum is large, move right pointer to left
        else:
            right -= 1

    return None


def two_sum_min(arr, num):

    arr.sort()
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer < right_pointer:
        c_sum = arr[left_pointer] + arr[right_pointer]

        if c_sum == num:
            return [arr[left_pointer], arr[right_pointer]]

        elif c_sum < num:
            left_pointer += 1

        else:
            right_pointer -= 1

    return None


arr = [1, 5, 2, 3, 2, 7, 4]
target = 6

print(two_sum(arr, target))
print(two_sum_min(arr, target))
