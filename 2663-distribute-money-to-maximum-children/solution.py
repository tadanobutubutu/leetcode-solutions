class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        
        money -= children  # Give 1 dollar to each child first
        count = money // 7
        rem = money % 7
        
        if count > children:
            return children - 1
        elif count == children:
            if rem == 0:
                return children
            else:
                return children - 1
        elif count == children - 1 and rem == 3:
            return count - 1
        else:
            return count

