class Solution:
    def maximumWealth(self, accounts):
        return max(map(sum,accounts))



Solution = Solution()
Solution.maximumWealth([[2,8,7],[7,1,3],[1,9,5]])

