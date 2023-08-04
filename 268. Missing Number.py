class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1]+1


a = Solution()
print(a.missingNumber([3,0,1])) #2
print(a.missingNumber([0,1]))  #2
print(a.missingNumber([9,6,4,2,3,5,7,0,1]))  #8
