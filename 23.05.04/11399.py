input()
lst = list(map(int, input().split()))
lst.sort() # 1 2 3 3 4
dp = [0]*len(lst) # 0 0 0 0 0
dp[0] = lst[0] # 1 0 0 0 0
for i in range(1, len(lst)):
    # i == 1 -> dp[1] = dp[0]+lst[1] = 3
    # i == 2 -> dp[2] = dp[1]+lst[2] = 3+3 = 6
    dp[i] = dp[i-1]+lst[i]
print(sum(dp))