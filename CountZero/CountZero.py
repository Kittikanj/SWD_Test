class Solution:
    def findZeroes(self, n):
        result = 0
        result += n // 5 if n >= 5 else 0
        result += n // 25 if n >= 25 else 0
        result += n // 125 if n >= 125 else 0
        result += n // 625 if n >= 625 else 0
        result += n // 3125 if n >= 3125 else 0
    
        return result
