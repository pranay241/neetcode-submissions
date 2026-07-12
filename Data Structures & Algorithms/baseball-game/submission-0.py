class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        answer = 0
        for c in operations:
            if c == "+":
                stack.append(stack[-1]+stack[-2])


            elif c == "C":
                stack.pop()

            elif c == "D":
                stack.append(2*stack[-1])

            else:
                stack.append(int(c))

        for i in range(len(stack)):

            answer += stack[i]

        return answer

               