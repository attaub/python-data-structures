# Process data from both ends towards center (or from center towards ends)
# An efficient way to reduce time complexity
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




arr = [1, 5, 2, 3, 2, 7, 4]
target = 6

print(two_sum(arr, target))

