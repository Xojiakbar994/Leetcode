class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        return [x for i in range(len(nums)) for x in [abs(sum(nums[:i]) - sum(nums[i+1:]))]]
    
a = Solution()

print(a.leftRightDifference(nums = [10,4,8,3]))
print(a.leftRightDifference(nums = [1]))


