class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]

        seen = set()
        for w in words:
            code = "".join(morse[ord(c) - ord('a')] for c in w)
            seen.add(code)

        return len(seen)

