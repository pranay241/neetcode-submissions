class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums1 = []

        for i in range(len(nums)):
            if nums[i]!=val:
                nums1.append(nums[i])
            
        for i in range(len(nums1)):
            nums[i] = nums1[i]


        return len(nums1)