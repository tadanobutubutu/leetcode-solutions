from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        last_group = None
        for word, group in zip(words, groups):
            if last_group is None or group != last_group:
                ans.append(word)
                last_group = group
        return ans

