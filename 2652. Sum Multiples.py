class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(3,n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                sum += i
        return sum
    
a = Solution()

print(a.sumOfMultiples(n=7))
print(a.sumOfMultiples(n=10))
print(a.sumOfMultiples(n=9))
