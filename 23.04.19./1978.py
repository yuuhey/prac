import math
n = input()
nums= list(map(int, input().split()))
def primenumber(s):
    if s == 1:
        return 0
    for i in range(2, int(math.sqrt(s))+1):
        if s%i==0:
            return 0
    return 1
count = 0
for num in nums:
    if primenumber(num)==1:
        count +=1
print(count)