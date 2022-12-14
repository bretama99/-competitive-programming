class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator, current_num = '+',0
        for i in range(len(s)):
            if s[i].isdigit():
                current_num = current_num*10 + int(s[i])
            if s[i] in '+-/*' or i == len(s)-1:
                if operator=='-':
                    stack.append(-current_num)
                elif operator == '+':
                    stack.append(current_num)
                elif operator == '*':
                    stack[-1]*=current_num
                elif operator == '/':
                    stack[-1]=int(stack[-1]/current_num)
                current_num = 0
                operator = s[i]
        return sum(stack)
