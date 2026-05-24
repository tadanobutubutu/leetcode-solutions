class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {" ": " "}
        curr_code = ord('a')
        
        for char in key:
            if char != " " and char not in mapping:
                mapping[char] = chr(curr_code)
                curr_code += 1
                if curr_code > ord('z'):
                    break
        
        return "".join(mapping[char] for char in message)

