class Solution:
    def reverse(self, x: int) -> int:
    
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        is_negative = x < 0
        x = abs(x)  # Work with the absolute value

        reversed_num = 0

        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        if is_negative:
            reversed_num *= -1

        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
        else:
            return reversed_num
