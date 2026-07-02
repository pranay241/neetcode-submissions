class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftmax = height[left]
        rightmax = height[right]
        water = 0

        while left<right:

            if height[left]<height[right]:
                leftmax = max(leftmax,height[left])
                water+= leftmax - height[left]
                left+=1


            else:
                rightmax = max(rightmax,height[right])
                water  += rightmax - height[right]
                right -=1

        return water