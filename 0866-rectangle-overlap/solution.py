class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # rec = [x1, y1, x2, y2]
        # 重ならない条件を列挙して、それ以外なら重なる
        return not (
            rec1[2] <= rec2[0] or  # rec1 が rec2 の左側に完全にある
            rec2[2] <= rec1[0] or  # rec2 が rec1 の左側に完全にある
            rec1[3] <= rec2[1] or  # rec1 が rec2 の下側に完全にある
            rec2[3] <= rec1[1]     # rec2 が rec1 の下側に完全にある
        )

