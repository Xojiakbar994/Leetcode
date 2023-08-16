class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maks = max(candies)
        ans = []
        for i in candies:
            if i + extraCandies >= maks:
                ans.append(True)
            else:
                ans.append(False)
        return ans


a = Solution()
print(a.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))
print(a.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))
print(a.kidsWithCandies(candies = [12,1,12], extraCandies = 10))
