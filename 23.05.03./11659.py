# 시간초과ver
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# for _ in range(m):
#     i, j = map(int,input().split())
#     print(sum(lst[i-1:j]))

# dp
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))

dp = [0] * (n + 1)
for k in range(n):
    dp[k+1] = dp[k] + array[k]

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])