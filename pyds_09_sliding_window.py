"""
Sliding windows:
Used to find subarrays/subsets satisfying a given condition
Useful to find a contiguous portion of the array or string

window either grows or shrinks as it moves across the sequence

Types: 
Fixed-size Sliding Window
Variable-size Sliding Window

Problems:
maximum sum subarray of size k
longest substring without repeating characters
find all anagrams in a string
subarrays with given sum
"""

## fixed-size sliding window
# find the maximum sum of any subarray of size k in an array

def max_sum_subarray(arr, k):
    if len(arr) < k: # edge case
        return None

    max_sum = sum(arr[:k])  
    window_sum = max_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  
        max_sum = max(max_sum, window_sum)  

    return max_sum

# variable-size sliding window
# longest substring without repeating characters


def longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


# example 
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))  


# example 
s = "abcabcbb"
print(longest_substring(s))  # Output: 3 (substring "abc")
