'''
From: Uber
Difficulty: Hard

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''


def get_product_arr_2(arr):
    total_product = 1
    for elt in arr:
        total_product *= elt
    
    product_arr = []
    for elt in arr:
        product_arr.append(total_product//elt)
    
    return product_arr


# without division
def get_product_arr(arr):
    n = len(arr)
    product_arr = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product*=arr[j]
        product_arr.append(product)
    return product_arr

if __name__ == "__main__":
    result = get_product_arr_2([1, 2, 3, 4, 5])
    print(result)

