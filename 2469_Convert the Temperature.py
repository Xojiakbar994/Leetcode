class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return(celsius+273.15, celsius * 1.80 + 32.00)
    
a = Solution()
print(a.convertTemperature(36.50))
print(a.convertTemperature(122.11))