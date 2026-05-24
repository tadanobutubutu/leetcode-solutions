from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_duration = 0
        best_employee = -1
        prev_time = 0
        
        for emp_id, leave_time in logs:
            duration = leave_time - prev_time
            if duration > max_duration:
                max_duration = duration
                best_employee = emp_id
            elif duration == max_duration:
                # 作業時間が同じ場合、より小さいIDの従業員を優先する
                if emp_id < best_employee:
                    best_employee = emp_id
            prev_time = leave_time
            
        return best_employee

