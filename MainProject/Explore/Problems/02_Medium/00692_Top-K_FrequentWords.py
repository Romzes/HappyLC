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

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass