def sum_num(num: int):
	a = 0
	num = str(num)
	for i in num:
		a += int(i) ** 2
	return a


class Solution:
	def isHappy(self, n: int) -> bool:
		num = set()
		while n != 1:
			n = sum_num(n)
			if n not in num:
				num.add(n)
			else:
				return False
		return True

b = Solution()
print(b.isHappy(19))  #True
print(b.isHappy(2))  #False
