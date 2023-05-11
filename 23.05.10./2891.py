n, s, r = map(int, input().split())
li_c = list(map(int, input().split()))
li_a = list(map(int, input().split()))
li_c.sort()
li_a.sort()
cnt = 0

for i in li_a:
    if i in li_c:
        del li_a[li_a.index(i)]
        del li_c[li_c.index(i)]

for i in li_c:
    if i-1 in li_a:
        li_a.remove(i-1)
    elif i+1 in li_a:
        li_a.remove(i+1)
    else:
        cnt += 1
print(cnt)