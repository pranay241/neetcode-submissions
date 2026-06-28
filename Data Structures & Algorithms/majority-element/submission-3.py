class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        n = len(nums)
        for number in nums:
            if number in frequency:
                frequency[number]+=1
            else:
                frequency[number] = 1

        for key in frequency:
            if frequency[key]>n/2:
                return key
