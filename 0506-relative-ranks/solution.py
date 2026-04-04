class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        indexed = [(s, i) for i, s in enumerate(score)]
        indexed.sort(reverse=True)

        result = [""] * n

        for rank, (_, idx) in enumerate(indexed, start=1):
            if rank == 1:
                result[idx] = "Gold Medal"
            elif rank == 2:
                result[idx] = "Silver Medal"
            elif rank == 3:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank)

        return result

