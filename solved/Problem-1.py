'''
From: Google
Difficulty: Easy

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def find_sum_couple(arr, k):
    for elt in arr:
        second = k - elt
        return second in arr
    return False

if __name__ == "__main__":
    result = find_sum_couple([10, 15, 3, 7], 17)
    print(result)

