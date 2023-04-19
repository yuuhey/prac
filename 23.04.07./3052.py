lst = []
for _ in range(10):
    lst.append(int(input())%42)
print(len(set(lst)))

# 숏코딩
# print(len({int(input())%42 for _ in range(10)}))