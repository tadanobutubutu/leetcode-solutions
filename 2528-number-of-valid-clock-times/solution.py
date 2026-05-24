class Solution:
    def countTime(self, time: str) -> int:
        def match(t_str: str, pattern: str) -> bool:
            for c1, c2 in zip(t_str, pattern):
                if c2 != '?' and c1 != c2:
                    return False
            return True

        count = 0
        # 00:00 から 23:59 までのすべての有効な時刻を探索
        for h in range(24):
            for m in range(60):
                t_str = f"{h:02d}:{m:02d}"
                if match(t_str, time):
                    count += 1
        return count

