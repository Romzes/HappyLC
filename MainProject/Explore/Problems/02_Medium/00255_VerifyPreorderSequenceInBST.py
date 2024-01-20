"""
255 (Medium) Verify Preorder Sequence in Binary Search Tree
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.
Constraints:
  1 <= preorder.length <= 10^4
  1 <= preorder[i] <= 10^4
  All the elements of preorder are unique.
"""

from typing import List
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        mn = float('-inf')
        j = -1  # вершина стека
        for i, v in enumerate(preorder):
            if v < mn: return False
            while j >= 0 and preorder[j] < v:
                mn = preorder[j]
                j -= 1
            preorder[j:=j+1] = v
        return True

sln = Solution()
print(sln.verifyPreorder(preorder=[0]))

sln = Solution()
print(sln.verifyPreorder(preorder=[5,2,1,3,6]))

sln = Solution()
print(sln.verifyPreorder(preorder=[5,2,6,1,3]))