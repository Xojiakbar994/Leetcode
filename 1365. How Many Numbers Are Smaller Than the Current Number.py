class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # small = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums [i] > nums [j]:
        #             count += 1
        #     small.append(count)
        # return small

        x =[]
        sort_num = sorted(nums)
        for i in range(0,len(nums)):
            x.append(sort_num.index(nums[i]))
        return x
    
a = Solution()

print(a.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
print(a.smallerNumbersThanCurrent(nums = [6,5,4,8]))
print(a.smallerNumbersThanCurrent(nums = [7,7,7,7]))
