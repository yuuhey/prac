li = [*map(int, input().split())]
max_l = 1
for i in range(1, min(li)+1):
    if li[0]%i==0 and li[1]%i==0:
        max_l = i

print(max_l)
print(li[0]*li[1]//max_l)