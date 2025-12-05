# #right to left:
s=input()
roman={
    "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
}
# # basic condition:
# # IV-(5-1)
# # VI-(6+1)
# # II-(1+1)
res=0
prev=0
for i in reversed(s):
    value=roman[i]
    if value<prev:
        res-=value
    else:
        res+=value
    prev=value
print(res)


#left to right:
s=input()
roman={
    "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000
}
# basic condition:
# IV-(5-1)
# VI-(6+1)
# II-(1+1)
total=0
for i in range(len(s)):
    if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
        total-=roman[s[i]]
    else:
        total+=roman[s[i]]
print(total)



