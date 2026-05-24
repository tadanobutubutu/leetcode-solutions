class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        candidates = []
        for i in range(len(number)):
            if number[i] == digit:
                candidates.append(number[:i] + number[i+1:])
        return max(candidates)

