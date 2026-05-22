class Solution:
    def replaceDigits(self, s: str) -> str:
        s_list = list(s)
        for i in range(1, len(s), 2):
            prev_char = s_list[i-1]
            shift_num = int(s_list[i])
            s_list[i] = chr(ord(prev_char) + shift_num)
        return "".join(s_list)

