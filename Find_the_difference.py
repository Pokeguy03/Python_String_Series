class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_char=Counter(s)
        t_char=Counter(t)
        for i in t_char:
            if t_char[i]!=s_char[i]:
                return i
        
