dic=defaultdict(int)
for i in a:
    dic[i]+=1
for i in b:
    if dic[i]>0:
        dic[i]-=1
k_count=sum(dic.values())
if k_count<=k:
    print("Yes")
else:
    print("No")
