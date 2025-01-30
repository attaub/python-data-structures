"""

DP: An optimization technique to break down complex problems
into simpler subproblems, store the results,
and reuse them to avoid redundant computations.

Useful for optimization problems and counting problems,
Eg: Fibonacci sequence, knapsack problem, shortest paths in graphs

Overlapping Subproblems:
Problems can be broken down into smaller subproblems that are solved repeatedly.
Example: Fibonacci sequence → fib(5) = fib(4) + fib(3), but fib(3) is computed multiple times.

Optimal Substructure
The optimal solution to a problem is built from the optimal solutions to its subproblems.
Example: Shortest path in a graph → If the shortest path from A → C passes through B, then the path A → B must also be shortest.

Two Approaches to DP

Top-Down (Memoization): Solve the problem recursively and store previously computed results.

Bottom-Up (Tabulation): Solve subproblems iteratively and store results in a table.
Fibonacci Series - The Classic DP Problem
Naive Recursive Approach (Exponential Time)

"""

# Naive Recursive Approach (Exponential Time)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))  

# Memoization (Top-Down DP)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(fib_memo(10))  



# Tabulation (Bottom-Up DP)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fib_tab(10))  # Output: 55

# Space-Optimized DP
def fib_space_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fib_space_optimized(10))  # Output: 55

############################################
############################################
# The 0/1 Knapsack Problem
""" Given N items with weights and values, and a knapsack with a weight capacity W, determine the maximum value that can be obtained.
"""
#  Recursive Approach
def knapsack(wt, val, W, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapsack(wt, val, W, n - 1)
    else:
        return max(
            val[n - 1] + knapsack(wt, val, W - wt[n - 1], n - 1),
            knapsack(wt, val, W, n - 1)
        )

wt = [2, 3, 4, 5]
val = [3, 4, 5, 6]
W = 5
print(knapsack(wt, val, W, len(wt)))  # Output: 7


# DP Approach (Tabulation)
def knapsack_dp(wt, val, W, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

print(knapsack_dp(wt, val, W, len(wt)))  # Output: 7


#############################################
# Longest Common Subsequence (LCS)
# Recursive Approach

def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1)
    else:
        return max(lcs(x, y, m - 1, n), lcs(x, y, m, n - 1))

x = "abcde"
y = "ace"
print(lcs(x, y, len(x), len(y)))  # Output: 3

# DP Approach (Tabulation)

def lcs_dp(x, y, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

print(lcs_dp(x, y, len(x), len(y)))  # Output: 3

############################################
# Coin Change Problem
# Given an amount N and a set of coins, find the minimum number of coins needed to make N.

# DP Approach (Tabulation)
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 2, 5], 11))  # Output: 3 (5+5+1)



