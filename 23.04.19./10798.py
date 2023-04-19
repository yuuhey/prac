lst = []
max_len = 0
for _ in range(5):
    s = str(input())
    lst.append(s)
    if len(s) > max_len:
        max_len = len(s)

for j in range(max_len):
    for i in range(5):
        try:
            print(lst[i][j], end="")
        except:
            continue