s=input()
n=len(s)
Tot_close=s.count(')')
close=Tot_close
open=0
found=False
for i in range(n):
    if open==close:
        print(i)
        found=True
        
    if s[i]=='(':
        open+=1
    else:
        close-=1

if not found:
    print("-1")
