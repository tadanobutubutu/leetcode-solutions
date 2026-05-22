class Solution:
    def minTimeToType(self, word: str) -> int:
        total_time = 0
        curr = 'a'
        for char in word:
            diff = abs(ord(char) - ord(curr))
            dist = min(diff, 26 - diff)
            total_time += dist + 1
            curr = char
        return total_time

