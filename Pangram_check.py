s=input().lower()
seen=set()
for i in s:
    if 'a'<=i<='z':
        seen.add(i)

if len(seen)==26:
    print("It is an Pangram")
else:
    print("None")
