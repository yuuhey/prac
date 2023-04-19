# import sys
# input=sys.stdin.readline
#
# input()
# lst1 = list(map(int, input().split()))
# input()
# lst2 = list(map(int, input().split()))
#
# for i in lst2:
#     if i in lst1:
#         print("1")
#     else:
#         print("0")

import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline
n = int(input())
a=list(map(int,input().split()))
m = int(input())
b=list(map(int,input().split()))
a.sort()
for x in b:
    right_index = bisect_right(a, x) # 정렬된 array에서 x가 위치하게될 오른쪽 인덱스(왼쪽값보다 크지만 오른쪽 값보다 작은 지점의 인덱스)
    left_index = bisect_left(a, x) # 정렬된 array에서 x가 위치하게될 왼쪽 인덱스(왼쪽값보다 크지만 오른쪽 값보다 작은 지점의 인덱스)
    if right_index > left_index: # right_index와 left_index가 차이가 난다면 해당 숫자가 존재하는 것이기에 1을 출력
        print(1)
    else: # right_index와 left_index가 차이가 난다면 해당 숫자가 업는 것이기에 0을 출력
        print(0)