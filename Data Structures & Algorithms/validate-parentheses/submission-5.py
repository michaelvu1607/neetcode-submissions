class Solution:
    def isValid(self, s: str) -> bool:
        complement = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        res = []

        for brack in s:
            if brack in complement.keys():
                if res != [] and complement[brack] in res[-1]:
                    res.pop()
                else:
                    return False
            else:
                res.append(brack)
        if res == []:
           return True
        else:
            return False