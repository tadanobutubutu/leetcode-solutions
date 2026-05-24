class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        if not words:
            return "#"
        
        # camelCase に変換
        camel_words = []
        for i, word in enumerate(words):
            if i == 0:
                camel_words.append(word.lower())
            else:
                if word:
                    camel_words.append(word[0].upper() + word[1:].lower())
        
        tag = "#" + "".join(camel_words)
        
        # 100文字に切り捨て
        return tag[:100]

