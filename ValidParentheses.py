class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            elif not stack:
                return False
            else:
                poped = stack.pop()
                if (char==')' and poped!='(') or (char =='}' and poped!='{') or (char==']' and poped!='['):
                    return False
        if not stack:
            return True
        return False