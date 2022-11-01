class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            elif s[i] == ')':
                temp = s[st[-1]:i + 1]
                s = s[:st[-1]] + temp[::-1] + s[i + 1:]
                del st[-1]
        return s.replace('(', '').replace(')','')