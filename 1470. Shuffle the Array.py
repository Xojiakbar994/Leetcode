class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[i+n])
        return new_list

a = Solution()

print(a.shuffle(nums = [2,5,1,3,4,7], n = 3))
print(a.shuffle(nums = [1,2,3,4,4,3,2,1], n = 4))
print(a.shuffle(nums = [1,1,2,2], n = 2))