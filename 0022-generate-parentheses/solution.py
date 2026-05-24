from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_str: str, open_cnt: int, close_cnt: int):
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            if open_cnt < n:
                backtrack(current_str + "(", open_cnt + 1, close_cnt)
                
            if close_cnt < open_cnt:
                backtrack(current_str + ")", open_cnt, close_cnt + 1)
                
        backtrack("", 0, 0)
        return result

