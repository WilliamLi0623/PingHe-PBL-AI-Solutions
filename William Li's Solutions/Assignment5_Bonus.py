# -*- coding: utf-8 -*-
"""William Li - Bonus Assignment - Knapsack Problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NCvtOtDR9_SYrUDhO9VuZQIxJ2pZBHgC

# The Knapsack Problem (10 Bonus Points on past and future HW problems)

**This Assignment is Completely Optional, and dynamic programming is not gonna be tested**

The knapsack problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
"""

# Preconditions of the problem
COST = 15
WEIGHTS = [1, 4, 1, 2, 12]
VALUES = [1, 10, 2, 2, 4]

"""## Dynamic Programming

Use dynamic programming and the idea of recusively dividing the original problem into its smaller counterparts to solve the knapsack problem.
"""

# Your code here
# Right, no hints, you are on your own :)
def knapsack(n):
	dp=[[0 for j in range(COST+1)] for i in range(n+1)];
	for i in range(1,n+1):
		for j in range(1,COST+1):
			dp[i][j]=dp[i-1][j];
			if j>=WEIGHTS[i-1] and dp[i][j]<dp[i-1][j-WEIGHTS[i-1]]+VALUES[i-1]:
				dp[i][j]=dp[i-1][j-WEIGHTS[i-1]]+VALUES[i-1];
	return dp[n][COST];
print(knapsack(5));