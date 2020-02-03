'''
From: Stripe
Difficulty: Hard

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def find_first_missing(arr):
        if not arr:
            return 1

        arr.append(0)
        n = len(arr)
        for i in range(n):
            if arr[i] <= 0 or arr[i] >= n:
                arr[i] = 0

        print(arr)

        for i in range(n):
            arr[arr[i] % n] += n

        print(arr)

        for i in range(1, n):
            if arr[i] < n:
                return i


print(find_first_missing([3, 4, 3, 1]))