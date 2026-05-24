class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def get_height(c1: int, c2: int) -> int:
            h = 0
            while True:
                required = h + 1
                if h % 2 == 0:
                    if c1 >= required:
                        c1 -= required
                    else:
                        break
                else:
                    if c2 >= required:
                        c2 -= required
                    else:
                        break
                h += 1
            return h

        return max(get_height(red, blue), get_height(blue, red))

