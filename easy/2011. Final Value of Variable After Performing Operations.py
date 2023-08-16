class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return operations.count('++X') + operations.count('X++') - operations.count('--X') - operations.count('X--')
    
a = Solution()

print(a.finalValueAfterOperations(operations = ["--X","X++","X++"]))
print(a.finalValueAfterOperations(operations = ["++X","++X","X++"]))
print(a.finalValueAfterOperations(operations = ["X++","++X","--X","X--"]))
