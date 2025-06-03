# 703 (Easy) K-th Largest Element in a Stream
"""
You are part of a university admissions office and need to keep track of the k-th highest test score from applicants in real-time.
This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.
You are tasked to implement a class which, for a given integer k,
maintains a stream of test scores and continuously returns the k-th highest test score after a new score has been submitted.
More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:
  KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
  int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

Constraints:
  0 <= nums.length <= 10^4
  1 <= k <= nums.length + 1
  -10^4 <= nums[i] <= 10^4
  -10^4 <= val <= 10^4
  At most 10^4 calls will be made to add.
"""

from typing import List
import heapq

# Runtime = 5 ms  Beats 97.18% ; Memory = 23.74 MB  Beats 46.35%
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        hp = self.hp = []  # min-heap
        if not nums: return
        heapify_flag = False
        for val in nums:
            if len(hp) < k:
                hp.append(val)
                if len(hp) == k:
                    heapq.heapify(hp)
                    heapify_flag = True
                continue
            if val <= hp[0]: continue
            heapq.heappushpop(hp, val)

        if not heapify_flag: heapq.heapify(hp)

    def add(self, val: int) -> int:
        k, hp = self.k, self.hp
        if len(hp) < k:
            heapq.heappush(hp, val)
        elif hp[0] < val:
            heapq.heappushpop(hp, val)
        return hp[0]


sln = KthLargest(k=3, nums=[4, 5, 8, 2])
print(sln.add(3))   # return 4
print(sln.add(5))   # return 5
print(sln.add(10))  # return 5
print(sln.add(9))   # return 8
print(sln.add(4))   # return 8

sln = KthLargest(k=4, nums=[7, 7, 7, 7, 8, 3])
print(sln.add(2))   # return 7
print(sln.add(10))  # return 7
print(sln.add(9))   # return 7
print(sln.add(9))   # return 8

sln = KthLargest(k=1, nums=[])
print(sln.add(-3))  # return -3
print(sln.add(-2))  # return -2
print(sln.add(-4))  # return -2
print(sln.add(0))   # return 0
print(sln.add(4))   # return 4