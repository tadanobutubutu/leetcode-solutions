class Solution:
    def minimumChairs(self, s: str) -> int:
        current_people = 0
        max_chairs = 0
        for char in s:
            if char == 'E':
                current_people += 1
                if current_people > max_chairs:
                    max_chairs = current_people
            elif char == 'L':
                current_people -= 1
        return max_chairs

