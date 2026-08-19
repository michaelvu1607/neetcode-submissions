class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in closeToOpen.values():
                stack.append(char)
            else:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False
