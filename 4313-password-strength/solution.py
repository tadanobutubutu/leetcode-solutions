class Solution(object):
    def passwordStrength(self, password):
        strength = 0
        distinct = set(password)
        for char in distinct:
            if 'a' <= char <= 'z':
                strength += 1
            elif 'A' <= char <= 'Z':
                strength += 2
            elif '0' <= char <= '9':
                strength += 3
            elif char in "!@#$":
                strength += 5
        return strength

