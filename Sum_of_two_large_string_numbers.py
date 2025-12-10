a="1234"
b="937"
i=len(a)-1
j=len(b)-1
carry=0
res=[]
while i>=0 or j>=0 or carry:
    d1=ord(a[i])-ord('0') if i>=0 else 0
    d2=ord(b[j])-ord('0') if j>=0 else 0

    total=d1+d2+carry
    carry=total//10
    res.append(str(total%10))
    i-=1
    j-=1
print(''.join(res))
