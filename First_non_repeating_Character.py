from collections import Counter
s=input()

li=(Counter(s))
for i in s:
    if li[i]==1:
        print(i)
        break
else:
    print("No repeatation")
