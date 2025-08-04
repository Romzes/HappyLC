from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums - DISTINCT values
        l, r = 0, len(nums)-1