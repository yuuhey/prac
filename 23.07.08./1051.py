import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(input())
if m<n:
    m, n = n, m
for i in range(n):
    if l[i][i] == l[i][i+]
