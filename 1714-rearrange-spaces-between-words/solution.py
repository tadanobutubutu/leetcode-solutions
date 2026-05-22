class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces_count = text.count(' ')
        words = text.split()
        words_count = len(words)
        
        if words_count == 1:
            return words[0] + ' ' * spaces_count
        
        between = spaces_count // (words_count - 1)
        extra = spaces_count % (words_count - 1)
        
        return (' ' * between).join(words) + ' ' * extra

