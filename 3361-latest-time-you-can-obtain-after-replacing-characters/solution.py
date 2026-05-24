class Solution:
    def findLatestTime(self, s: str) -> str:
        s_list = list(s)
        
        # s[0] の判定
        if s_list[0] == '?':
            if s_list[1] == '?' or s_list[1] in ('0', '1'):
                s_list[0] = '1'
            else:
                s_list[0] = '0'
                
        # s[1] の判定
        if s_list[1] == '?':
            if s_list[0] == '1':
                s_list[1] = '1'
            else:
                s_list[1] = '9'
                
        # s[3] の判定
        if s_list[3] == '?':
            s_list[3] = '5'
            
        # s[4] の判定
        if s_list[4] == '?':
            s_list[4] = '9'
            
        return "".join(s_list)

