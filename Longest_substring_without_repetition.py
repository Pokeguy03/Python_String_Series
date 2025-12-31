class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setter=set()
        l=0
        count=0
        for i in range(len(s)):
            while s[i] in setter:
                setter.remove(s[l])
                l+=1
            setter.add(s[i])
            count=max(count,i-l+1)
        return count
        
