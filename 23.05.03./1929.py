# 시간초과ver
# m, n = map(int, input().split())
# for i in range(m,n+1):
#     breaker = False
#     for j in range(2,i):
#         if i%j==0:
#             breaker = True
#             break
#     if breaker ==True:
#         continue
#     print(i)

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

m, n = map(int, input().split())
for i in range(m,n+1):
    if isPrime(i) == True:
        print(i)