class Solution:
    def isValid(self, s: str) -> bool:
        mapings = {'}':'{',')':'(',']':'['}
        stack = []

        for char in s:
            if char in mapings:
                if len(stack) == 0 or mapings[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0 
