# Medium 71. Simplify Path
# Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system,
# convert it to the simplified canonical path.

class Solution:
    def simplifyPath(self, path):
        stack, parts = [], [s for s in path.split(sep='/') if s not in ('', '.')]
        for s in parts:
            if s == '..':
                if stack: stack.pop()
            else: stack.append(s)
        return '/' + '/'.join(stack)


sln = Solution()
print(sln.simplifyPath(path=r'/.'))

sln = Solution()
print(sln.simplifyPath(path=r'../../home/././foo/../abc'))

