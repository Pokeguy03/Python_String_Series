#string 121(My approach)
s=input()
a=s
if s[::-1]==s:
    print("Its is an Palindrome")
else:
    print("None")

#Two Pointer Approach:
s=input()
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print(0)
        break
    left+=1
    right-=1
else:
    print(1)


