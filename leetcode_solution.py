# Week3: leetcode 20.Valid Parentheses
class Solution:
    def isValid(self,s):
        stack = []
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char in brackets:
                if not stack or stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
