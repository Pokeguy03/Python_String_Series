# aaaaabbbcc
# count the consecutive character
# a5b3c2
# convert to hexadecimal using format(count,'x')
# then reverse the numbers

s=input()
i=0
n=len(s)
joint=" "
while i<n:
    value=s[i]
    count=1
    while i+1<n and s[i]==s[i+1]:
        count+=1
        i+=1
    hexa=format(count,'x')
    joint+=value+hexa
    i+=1
reverse=joint[::-1]
print(reverse)
