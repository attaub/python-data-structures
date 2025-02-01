""" 
2D DP is essential when dealing with
grids, matrices, or sequences with two varying indices .

A 2D DP solution involves creating a 2D table (dp[][]) where:

dp[i][j] represents the solution to the subproblem involving the first i and j elements.

Transition relations help compute dp[i][j] using previously computed values.

The base case defines the initial values of the DP table.

Common Problems Using 2D DP

"""

"""
Longest Common Subsequence (LCS)
Given two strings X and Y, find the length of their longest common subsequence.

Recurrence Relation:
If X[i] == Y[j], then dp[i][j] = 1 + dp[i-1][j-1]
Otherwise, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""
def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print(longest_common_subsequence(X, Y))  # Output: 4


"""
Edit Distance (Levenshtein Distance)
Given two strings, find the minimum number of operations
(insertions, deletions, substitutions) to convert one string into another.

Recurrence Relation:
If X[i] == Y[j], then dp[i][j] = dp[i-1][j-1]
Otherwise, dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
"""

def edit_distance(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

X = "sunday"
Y = "saturday"
print(edit_distance(X, Y))  # Output: 3


"""
Unique Paths in a Grid

Problem: Given an m x n grid, find the number of unique paths from the top-left to the bottom-right, moving only right or down.

Recurrence Relation:

dp[i][j] = dp[i-1][j] + dp[i][j-1]

Base case: dp[0][j] = dp[i][0] = 1


"""
def edit_distance(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

X = "sunday"
Y = "saturday"
print(edit_distance(X, Y))  # Output: 3

"""
Unique Paths in a Grid

Problem: Given an m x n grid, find the number of unique paths from the top-left to the bottom-right, moving only right or down.

Recurrence Relation:

dp[i][j] = dp[i-1][j] + dp[i][j-1]

Base case: dp[0][j] = dp[i][0] = 1

"""

def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

print(unique_paths(3, 7))  # Output: 28


"""
Optimizing Space Complexity

For some problems, storing the entire dp table is unnecessary. We can optimize space by using only the previous row or column.

Example: Optimizing LCS space complexity

"""
def optimized_lcs(X, Y):
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    
    return prev[n]
