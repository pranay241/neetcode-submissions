class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for n in nums:
            ans.append(n)
        return ans*2
