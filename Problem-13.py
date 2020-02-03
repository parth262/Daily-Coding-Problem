'''
From: Amazon
Difficulty: Hard

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''

def helper(str, n):
    lstr = ""
    ucount = 0
    for ch in str:
        if ch not in lstr:
            if ucount == n:
                break
            ucount += 1
        lstr += ch
    return lstr

def longest_unique_n(str, n):
    lstr = ""
    for i in range(len(str)-n):
        tstr = helper(str[i:], n)
        if len(tstr) > len(lstr):
            lstr = tstr
    return lstr    

print(longest_unique_n("abcba", 2))
