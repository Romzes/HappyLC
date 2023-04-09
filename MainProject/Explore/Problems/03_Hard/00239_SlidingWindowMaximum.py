# Hard 239. Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque(maxlen=k)  # nums-indexes
        for i in range(k): self.q_add_i(q, nums, i)
        res = (len(nums)-k+1) * [None]
        res[0], j = nums[q[0]], 1
        for i in range(k, len(nums)):
            if q[0] <= i-k: q.popleft()
            self.q_add_i(q, nums, i)
            res[j] = nums[q[0]]
            j += 1
        return res

    def q_add_i(self, q, nums, i):
        while q and nums[q[-1]] <= nums[i]: q.pop()
        q.append(i)

sln = Solution()
print(sln.maxSlidingWindow(nums=[3,2,1,4], k=3))

sln = Solution()
print(sln.maxSlidingWindow(nums=[1,3,-1,-3,5,3,6,7], k=3))
