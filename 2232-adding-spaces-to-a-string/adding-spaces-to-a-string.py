class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        len_spaces, len_s = len(spaces), len(s)
        t=[' ']*(len_spaces+len_s)
        j=0
        for i, c in enumerate(s):
            if j<len_spaces and i==spaces[j]:
                j+=1
            t[i+j]=s[i]
        return "".join(t)       