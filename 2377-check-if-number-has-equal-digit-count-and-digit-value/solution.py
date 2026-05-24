class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            expected_count = int(num[i])
            actual_count = num.count(str(i))
            if actual_count != expected_count:
                return False
        return True

