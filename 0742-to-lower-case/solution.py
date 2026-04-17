class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for ch in s:
            if 'A' <= ch <= 'Z':
                result.append(chr(ord(ch) + 32))
            else:
                result.append(ch)
        return "".join(result)

