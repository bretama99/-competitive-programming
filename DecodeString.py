class Solution:
    def decodeString(self, s: str) -> str:
#         def decode(index):
#             # cur = index
#             num = ""
#             i = index
#             while s[i].isdigit():
#                 num = num + s[i]
#                 i+=1
#             multiplier = int(num)
#             cur = i
#             cur += 1
#             chars = []
#             while cur < len(s) and s[cur] != ']':
#                 if s[cur].isalpha():
#                     chars.append(s[cur])
#                     cur += 1
#                 else:
#                     decodedString, nextCur = decode(cur)  # cc
#                     chars.append(decodedString)
#                     cur = nextCur
#             return multiplier * (''.join(chars)), cur + 1

#         cur = 0
#         result = []
#         while cur < len(s):
#             if s[cur].isdigit():
#                 decoded, nextIndex = decode(cur)
#                 cur = nextIndex
#                 result.append(decoded)
#             else:
#                 result.append(s[cur])
#                 cur += 1
#         return ''.join(result)
        stack = []
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1]!='[':
                    substr = stack.pop()+substr
                stack.pop()
                num=""
                while stack and stack[-1].isdigit():
                    num=stack.pop()+num
                stack.append(int(num)*substr)
        return ("".join(stack))
        
