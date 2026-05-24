class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        seen = set()
        count = 0
        for w in words:
            rev = w[::-1]
            if rev in seen:
                count += 1
                seen.remove(rev)
            else:
                seen.add(w)
        return count

