class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[i] for i in nums]
    
a = Solution()
print(a.buildArray([0,2,1,5,3,4]))
print(a.buildArray([5,0,1,2,3,4]))