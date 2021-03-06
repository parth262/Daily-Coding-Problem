'''
From: Amazon
Difficulty: Hard

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

# recursive approach
def count_steps(n):
    if n <= 1:
        return 1


    return count_steps(n-1) + count_steps(n-2)

# print(count_steps(4))

# DP approach
def count_steps_dp(n):
    if n <= 1:
        return 1
    nums = [-1]*(n+1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    return nums[n]

# print(count_steps_dp(4))

# additional case
def count_steps_X(n, step_set=[1, 2]):
    if n == 0:
        return 1
    
    total = 0
    for i in step_set:
        if n-i >= 0:
            total += count_steps_X(n-i, step_set)
    return total

print(count_steps_X(4, [1, 3, 5]))
            

