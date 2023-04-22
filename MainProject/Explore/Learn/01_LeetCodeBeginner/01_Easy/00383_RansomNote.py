# Easy 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote, magazine):
        md = {}
        for c in magazine: md[c] = md.get(c,0)+1
        for c in ransomNote:
            cnt = md.get(c,0)
            if cnt == 0: return False
            else: md[c] -= 1
        return True

sln = Solution()
print(sln.canConstruct(ransomNote='a', magazine='b'))

sln = Solution()
print(sln.canConstruct(ransomNote='aa', magazine='ab'))

sln = Solution()
print(sln.canConstruct(ransomNote='aa', magazine='aab'))