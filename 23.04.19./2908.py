lst = list(map(str, input().split()))
for i in range(len(lst)):
    lst[i] = "".join(reversed(lst[i]))
if lst[0]>lst[1]:
    print(lst[0])
elif lst[1]>lst[0]:
    print(lst[1])