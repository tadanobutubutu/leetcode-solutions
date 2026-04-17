import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 単語をすべて小文字にして抽出（英字以外は区切り扱い）
        words = re.findall(r"[a-zA-Z]+", paragraph.lower())

        banned_set = set(banned)

        count = Counter(w for w in words if w not in banned_set)

        # 最頻出の単語を返す
        return count.most_common(1)[0][0]

