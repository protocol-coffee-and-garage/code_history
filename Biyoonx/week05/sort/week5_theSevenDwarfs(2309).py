import sys
read = sys.stdin.readline

h_list = sorted(list(int(read()) for _ in range(9)))

all_sum = sum(h_list)
result = []

for h in h_list:
    sub_target = all_sum - h - 100
    if sub_target <= 0 or sub_target == h:
        continue
    if sub_target in h_list:
        # filter() 함수로 필터링
        result = filter(lambda x: x != h and x != sub_target, h_list)
        print('\n'.join(map(str, result)))

        # 직접 값 제거(결과 출력 대상 리스트가 달라짐)
        # h_list.remove(h)
        # h_list.remove(sub_target)
        # print('\n'.join(map(str, h_list)))

        # 차집합으로 제거
        # result = list(set(h_list) - {h, sub_target})
        # print('\n'.join(map(str, result)))

        break