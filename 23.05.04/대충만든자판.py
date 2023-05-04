def solution(key, tar):
    answer = []
    dic = {}

    for i in key:                           # keymap의 원소(문자열)를 하나씩 가져온다.
        tmp = list(set(list(i)))            # list - set - list를 통해 unique하게 만들어준다.
        for j in tmp:                       # 유니크하게 만든 값을 하나씩 돌면서 딕셔너리에 최소횟수를 담는다.
            if(j in dic):                   # 딕셔너리에 키값이 있으면 최소값으로 대체
                dic[j] = min(dic[j], i.index(j) + 1)
            else:                           # 없으면 생성
                dic[j] = i.index(j) + 1

    for i in tar:                           # target의 원소(문자열)를 하나씩 가져온다
        tmp = 0                             # 횟수를 저장하기위한 변수
        for j in i:                         # 해당하는 문자열에 대한 딕셔너리 value를 tmp에 더하기
            if(j in dic):
                tmp += dic[j]
            else:                           # 해당하는 key값을 딕셔너리에서 찾을 수 없으면 tmp를 -1로 변경
                tmp = -1                    # tmp를 -1로 변경
                break                 ####### for문을 나간다.
        answer.append(tmp)                  # answer에 횟수 또는 -1 추가

    return answer