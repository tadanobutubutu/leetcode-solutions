class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(st):
            skip = 0
            for c in reversed(st):
                if c == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield c

        return all(a == b for a, b in zip(build(s), build(t))) and \
               len(list(build(s))) == len(list(build(t)))

