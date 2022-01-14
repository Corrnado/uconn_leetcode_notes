# Counting number of digit one from 0 to a given number. Dynamic programming
class Solution:
    def countDigitOne(self, n: int) -> int:
        vals = [1] 
        for i in range(1,10):
            vals.append(vals[-1]*10 + 10**i)
        def count(v):
            if v < 10:
                return 1 if v >=1 else 0
            digit = v
            lvl = 0
            while (digit//10) > 0:
                digit = digit // 10
                lvl += 1
            reminder = v - digit*10**lvl
            return vals[lvl-1]*digit + (1 if digit>1 else 0)*10**lvl \
                    + (reminder+1 if digit==1 else 0) + count(reminder)        
        return count(n)
            