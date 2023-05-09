li = list(map(int, input().split()))
c = int(input())
n = int(input())
if li[0]*n + li[1] <= c*n and c>=li[0]:
    print(1)
else:
    print(0)