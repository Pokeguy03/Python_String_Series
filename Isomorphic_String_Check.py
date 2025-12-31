t="abb"
s="xzy"
m1={}
m2={}
for i in range(len(s)):
    c1=s[i]
    c2=t[i]
    if c1 in m1 and m1[c1]!=c2:
        print(False)
    if c2 in m2 and m2[c2]!=c1:
        print(False)
    m1[c1]=c2
    m2[c2]=c1
print(True)
        
Leetcode:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()
        if len(pattern)!=len(word):
            return False
        ctow={}
        wtoc={}
        for i in range(0,len(word)):
            if pattern[i] not in ctow:
                ctow[pattern[i]]=word[i]
            elif pattern[i] in ctow:
                if ctow[pattern[i]]==word[i]:
                    continue
                else:
                    return False
            if word[i] not in wtoc:
                wtoc[word[i]]=pattern[i]
            elif word[i] in wtoc:
                if wtoc[word[i]]==pattern[i]:
                    continue
                else:
                    return False
        return True

                    
        
