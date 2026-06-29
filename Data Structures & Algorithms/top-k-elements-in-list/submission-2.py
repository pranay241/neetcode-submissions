class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        n = len(nums)
        list = []

        for number in nums:
            if number in frequency:
                frequency[number]+=1
            else:
                frequency[number] = 1

        sorted_freq = sorted(frequency.items(),key = lambda x:x[1],reverse=True)

        for key in range(k):
            list.append(sorted_freq[key][0])
        return list
                

        