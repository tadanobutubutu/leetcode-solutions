class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {name: i for i, name in enumerate(list1)}
        best = float('inf')
        res = []

        for j, name in enumerate(list2):
            if name in index_map:
                s = j + index_map[name]
                if s < best:
                    best = s
                    res = [name]
                elif s == best:
                    res.append(name)

        return res

