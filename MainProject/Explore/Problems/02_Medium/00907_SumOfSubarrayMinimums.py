"""
907 (Medium) Sum of Subarray Minimums
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 10^9 + 7.
Constraints:
  1 <= arr.length <= 3 * 10^4
  1 <= arr[i] <= 3 * 10^4
"""

from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """ на обработку приходит элемент a = arr[i]
        stack = [(k, a_k, s_k)]
        a_k = arr[k] элементы из arr[0 ; i-1] образуют монотонно возрастающий stack
        s_k = sum(arr[k ; k]) + sum(arr[k-1 ; k]) + ... sum(arr[0 ; k])
        res = sum(sum(arr[j1 ; j2])) , 0 <= j1 <= j2 <= i-1
        """
        res = 0; stack = []
        for i, a in enumerate(arr):
            while stack:
                k, a_k, s_k = stack[-1]
                if a_k >= a:
                    stack.pop()
                else:
                    # a_k < a и min(arr[k+1 ; i]) = a
                    s_i = s_k + (i-k)*a
                    res += s_i
                    stack.append((i, a, s_i))
                    break
            else:
                # min(arr[0 ; i]) = a
                s_i = (i+1)*a
                res += s_i
                stack.append((i, a, s_i))
        return res % (10**9 + 7)

sln = Solution()
print(sln.sumSubarrayMins(arr=[3,1,2,4]))

sln = Solution()
print(sln.sumSubarrayMins(arr=[11,81,94,43,3]))