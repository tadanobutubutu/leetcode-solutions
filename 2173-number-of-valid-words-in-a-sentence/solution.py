class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(word: str) -> bool:
            # 1. No digits
            if any(c.isdigit() for c in word):
                return False
            
            # 2. Hyphens check
            hyphen_count = word.count('-')
            if hyphen_count > 1:
                return False
            if hyphen_count == 1:
                idx = word.index('-')
                if idx == 0 or idx == len(word) - 1:
                    return False
                if not (word[idx-1].islower() and word[idx+1].islower()):
                    return False
            
            # 3. Punctuation check
            puncs = {'!', '.', ','}
            punc_count = sum(1 for c in word if c in puncs)
            if punc_count > 1:
                return False
            if punc_count == 1:
                if word[-1] not in puncs:
                    return False
            
            return True

        return sum(1 for word in sentence.split() if is_valid(word))

