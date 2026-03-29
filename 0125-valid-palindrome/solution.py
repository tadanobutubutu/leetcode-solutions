class Solution:
    # 型ヒントなしでSyntaxError回避
    def isPalindrome(self, s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]
