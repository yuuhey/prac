from sys import stdin

tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' # 10진수를 넘어갈 때 표현할 언어 저장
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

n, b = map(int, stdin.readline().split())
answer = ''

while n != 0:
    answer += str(tmp[n%b]) # n을 계산할 진법수 b로 나눈 나머지를 문자열 저장
    n = n//b # 몫으로 다시 업데이트

print(answer[::-1]) # 뒤에서부터 출력