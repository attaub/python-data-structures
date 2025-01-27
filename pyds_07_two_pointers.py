# Process data from both ends towards center or vice versa


def two_sum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1

    while l < r:
        cur_s = nums[l] + nums[r]

        if cur_s == target:
            return [nums[l], nums[r]]

        elif cur_s < target:
            l += 1

        else:
            r -= 1
    return None


nums = [1, 5, 2, 3, 2, 7, 4]
two_sum(nums, 6)
two_sum(nums, 11)
