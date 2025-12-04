#My approach
s=input()
print(s[::-1])


#two pointer
s=input()
left=0
right=len(s)-1
while left<right:
    s=list(s)
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1
print(''.join(s))
