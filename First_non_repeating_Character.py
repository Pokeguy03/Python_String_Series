from collections import Counter
s=input()

li=(Counter(s))
for i in s:
    if li[i]==1:
        print(i)
        break
else:
    print("No repeatation")



Leetcode:
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        li=Counter(s)
        for i in range(len(s)):
            if li[s[i]]==1:
                return i
                break
           
        return -1
        
