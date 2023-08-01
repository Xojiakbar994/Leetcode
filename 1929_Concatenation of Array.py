class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums.extend(nums)
        return nums
    

a = Solution()
print(a.getConcatenation([1,2,1]))
print(a.getConcatenation([1,3,2,1]))
