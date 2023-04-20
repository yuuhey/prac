lst = []
for _ in range(int(input())):
    lst.append(str(input()))
lst = list(set(lst))
lst.sort() #알파벳 순으로 정렬
lst.sort(key=len) #그 다음 길이로 정렬 -> 후에 적용 된 게 우선
for i in lst: print(i)