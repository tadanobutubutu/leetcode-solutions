class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def date_to_day(date_str: str) -> int:
            m, d = map(int, date_str.split('-'))
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return sum(days_in_month[:m-1]) + d
            
        start_a = date_to_day(arriveAlice)
        end_a = date_to_day(leaveAlice)
        start_b = date_to_day(arriveBob)
        end_b = date_to_day(leaveBob)
        
        return max(0, min(end_a, end_b) - max(start_a, start_b) + 1)

