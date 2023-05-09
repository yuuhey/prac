input()
li = list(map(int, input().split()))
x = int(input())
li.sort()
c = 0
for i in range(1, len(li)//2+1):
    if x-li[i] in li:
        c +=1
print(c)