class Solution:
    def reverseByType(self, s: str) -> str:
        letters = [c for c in s if c.islower()]
        specials = [c for c in s if not c.islower()]
        
        letters_iter = iter(letters[::-1])
        specials_iter = iter(specials[::-1])
        
        ans = []
        for c in s:
            if c.islower():
                ans.append(next(letters_iter))
            else:
                ans.append(next(specials_iter))
                
        return ''.join(ans)

