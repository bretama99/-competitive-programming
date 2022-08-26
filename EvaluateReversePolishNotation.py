import math
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for i in tokens:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(int(i))
    return int(round(stack.pop()))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))