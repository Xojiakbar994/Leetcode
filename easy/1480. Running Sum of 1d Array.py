class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(sum(nums[0:i+1]))
        return ans
    
a = Solution()
print(a.runningSum(nums = [1,2,3,4]))
print(a.runningSum(nums = [1,1,1,1,1]))
print(a.runningSum(nums = [3,1,2,10,1]))