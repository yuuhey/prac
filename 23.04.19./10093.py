a, b = map(int,input().split())
if a>b:
    a, b = b, a
if a==b or a+1==a:
    print(0)
else:
    print(b-a-1)
for i in range(a+1, b):
    print(i, end=" ")