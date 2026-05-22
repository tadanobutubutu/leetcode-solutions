class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_dict = {m: f"{i:02d}" for i, m in enumerate(months, 1)}
        
        day_str, month_str, year_str = date.split()
        
        day = f"{int(day_str[:-2]):02d}"
        month = month_dict[month_str]
        year = year_str
        
        return f"{year}-{month}-{day}"

