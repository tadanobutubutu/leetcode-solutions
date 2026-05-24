class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        # Find the first digit that is not '9'
        d_max = None
        for char in num_str:
            if char != '9':
                d_max = char
                break
        
        if d_max is not None:
            max_val = int(num_str.replace(d_max, '9'))
        else:
            max_val = num
            
        # The first digit must be replaced with '0' for the minimum value
        d_min = num_str[0]
        min_val = int(num_str.replace(d_min, '0'))
        
        return max_val - min_val

