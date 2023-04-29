# 그냥 평소 방식 -> 시간초과 에러
input()
n_lst = list(map(int, input().split()))
input()
m_lst = list(map(int, input().split()))
for i in m_lst:
    print(n_lst.count(i), end=' ')

# 방법 1 : bisect 사용
from bisect import bisect_left, bisect_right
from sys import stdin

n = stdin.readline().rstrip()
n_lst = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
m_lst = list(map(int, stdin.readline().split()))
n_lst.sort()

def count_num(lst, value):
    right_index = bisect_right(lst, value)
    left_index = bisect_left(lst, value)
    return right_index-left_index

for i in m_lst:
    print(count_num(n_lst, i), end=' ')

# 방법 2 : Counter 사용
from collections import Counter
from sys import stdin

n = stdin.readline().rstrip()
n_lst = list(map(int, stdin.readline().split()))
m = stdin.readline().rstrip()
m_lst = list(map(int, stdin.readline().split()))

count = Counter(n_lst)

for i in m_lst:
    if i in count:
        print(count[i], end=' ')
    else:
        print(0, end=' ')