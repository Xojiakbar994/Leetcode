class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        x = sum(nums)
        y = 0
        for i in nums:
            for j in str(i):
                y += int(j)
        return abs(x - y)

a = Solution()
print(a.differenceOfSum(nums = [1,15,6,3]))
print(a.differenceOfSum(nums = [1,2,3,4]))

