"""
https://leetcode.com/company/yandex/discuss/3305189/Yandex-or-OA-or-Count-common-elements-for-prefixes
Given two lists of integers of length N.
You need to return the number of common elements for all prefixes of length 1 to N.
Example 1:
Input:
N = 4
A = [1,1,2,3]
B = [2,1,3,1]
Output: [0,1,2,3]

Example 2:
Input:
N = 4
A = [1,1,1,1]
B = [2,1,1,1]
Output: [0,1,1,1]

Note: solve with O(N) time and space complexity.
"""

def calc_nums(arr1, arr2):
    n = len(arr1)
    res_arr = n * [0]; res_set = set()
    stat1, stat2 = {}, {}
    for i in range(n):
        v1, v2 = arr1[i], arr2[i]
        if v1 not in stat1: stat1[v1] = i
        if v2 not in stat2: stat2[v2] = i
        if stat1.get(v2, n) <= i: res_set.add(v2)
        if stat2.get(v1, n) <= i: res_set.add(v1)
        res_arr[i] = len(res_set)
    return res_arr

arr1 = [1,1,2,3]
arr2 = [2,1,3,1]
print(calc_nums(arr1, arr2))

arr1 = [1,1,1,1]
arr2 = [2,1,1,1]
print(calc_nums(arr1, arr2))