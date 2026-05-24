class Solution:
    def countEven(self, num: int) -> int:
        def is_even_digit_sum(x: int) -> bool:
            return sum(int(d) for d in str(x)) % 2 == 0
        
        count = 0
        for i in range(1, num + 1):
            if is_even_digit_sum(i):
                count += 1
        return count

