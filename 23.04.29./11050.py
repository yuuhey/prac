# 이건 왜 안되지
# n, k = map(int, input().split())
# if k>n/2:
#     k = n-k
# sum1 = n
# sum2 = 1
# for i in range(1,k):
#     sum1 *= n-i
#     sum2 *= i+1
# print(int(sum1/sum2))

#맞은 풀이
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

divisor = 1
for i in range(2, K+1):
    divisor *= i

print(result // divisor)