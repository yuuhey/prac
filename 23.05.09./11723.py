from sys import stdin

input = stdin.readline
S = set()
for _ in range(int(input())):
    li = list(input().split())
    if li[0] == 'add':
        S.add(int(li[1]))
    elif li[0] == 'remove':
        S.discard(int(li[1]))
    elif li[0] == 'check':
        if int(li[1]) in S:
            print(1)
        else: print(0)
    elif li[0] == 'toggle':
        if int(li[1]) in S:
            S.discard(int(li[1]))
        else:
            S.add(int(li[1]))
    elif li[0] == 'all':
        S = set(i+1 for i in range(20))
    elif li[0] == 'empty':
        S = set()