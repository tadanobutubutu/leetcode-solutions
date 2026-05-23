class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(token) for token in s.split() if token.isdigit()]
        return all(nums[i] < nums[i+1] for i in range(len(nums) - 1))

