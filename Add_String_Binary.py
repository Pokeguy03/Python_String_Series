#Without built-in 
a="1011"
b="0101"
carry=0
res=[]
i=len(a)-1
j=len(b)-1
while i>=0 or j>=0 or carry:
    total=carry
    if i>=0:
        total+=int(a[i])
        i-=1
    if j>=0:
        total+=int(b[j])
        j-=1
    res.append(str(total%2))
    carry=total//2
print(''.join(reversed(res)))


#Easy one
a="1011"
b="0101"
c=bin(int(a,2)+int(b,2))
print(c[2:])
