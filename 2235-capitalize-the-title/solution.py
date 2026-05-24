class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        ans = []
        for w in words:
            if len(w) <= 2:
                ans.append(w.lower())
            else:
                ans.append(w.capitalize())
        return " ".join(ans)

