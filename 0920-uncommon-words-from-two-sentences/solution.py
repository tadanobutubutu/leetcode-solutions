from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter((s1 + " " + s2).split())
        return [w for w in cnt if cnt[w] == 1]

