# 692 (Medium) Top K Frequent Words
"""
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?

Constraints:
  1 <= words.length <= 500
  1 <= words[i].length <= 10
  words[i] consists of lowercase English letters.
  k is in the range [1, The number of unique words[i]]
"""

from typing import List
import heapq

class Freq:
    def __init__(self, w, cnt):
        self.w, self.cnt = w, cnt

    def __lt__(self, other):
        d = self.cnt - other.cnt
        return d < 0 or (d == 0 and self.w > other.w)

# Runtime = 0 ms  Beats 100.00%  ;  Memory = 18.12 MB  Beats 20.21%
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        for w in words: counter[w] = counter.get(w, 0) + 1
        hp = []  # min-heap list[Freq]
        for w, cnt in counter.items():
            freq = Freq(w, cnt)
            if len(hp) < k:
                hp.append(freq)
                if len(hp) == k: heapq.heapify(hp)
                continue
            # len(hp) == k
            if freq < hp[0]: continue
            heapq.heappushpop(hp, freq)
        hp.sort(reverse=True)
        return [freq.w for freq in hp]


sln = Solution()
print(sln.topKFrequent(words=["i","love","leetcode","i","love","coding"], k=2))
# Output: ["i","love"]

sln = Solution()
print(sln.topKFrequent(words=["the","day","is","sunny","the","the","the","sunny","is","is"], k=4))
# Output: ["the","is","sunny","day"]

sln = Solution()
print(sln.topKFrequent(words=["i","love","leetcode","i","love","coding"], k=3))
# Output: ["i","love","coding"]