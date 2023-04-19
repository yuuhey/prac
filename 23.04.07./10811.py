n, m = map(int, input().split())
*lst, = range(n+1)
for _ in range(m):
    i, j = map(int, input().split())
    lst[i:j+1] = reversed(lst[i:j+1])
print(*lst[1:])
