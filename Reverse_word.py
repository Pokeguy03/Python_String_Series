#My approach
s=input().split()
a=(s[::-1])
print(' '.join(a))

# #two Pointer:
s=input().split()
left=0
right=len(s)-1
while left<right:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print(' '.join(s))
