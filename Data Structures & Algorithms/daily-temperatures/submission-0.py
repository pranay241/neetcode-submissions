class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []

        for i , t  in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackT,stackIND = stack.pop()
                output[stackIND] = (i - stackIND)
            stack.append([t,i])

        return output