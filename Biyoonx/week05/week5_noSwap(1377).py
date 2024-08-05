import sys
read = sys.stdin.readline

n = int(read())
num_list = [(int(read()), i) for i in range(n)]
# 딕셔너리로 받으면 같은 값이 여러 번 입력되어 키가 중복되는 경우 값이 덮어씌워져서 유실되는 문제 발생
# num_list = {int(read()): i for i in range(n)}

# 시간 초과
'''
for idx in range(n):
    changed = False
    for i in range(1, n):
        if num_list[i - 1] > num_list[i]:
            changed = True
            num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]
    if not changed:
        print(idx + 1)
        break
'''

# 숫자를 오름차순으로 정렬하므로 한 턴에 숫자가 오른쪽으로는 여러 번 이동할 수는 있으나 왼쪽으로는 한 턴에 최대 한 번만 이동 가능함 >> 숫자가 왼쪽으로 이동한 최대 횟수 + 1을 구하면 됨(+swap이 일어나지 않는 턴도 포함해야하므로 +1을 할 것)
# 참고 : https://scarlettb.tistory.com/m/114

# num_dict = {val: idx for idx, val in enumerate(num_list)}
# .sort()나 sorted() 모두 튜플이 들어가면 첫 번째 요소를 기준으로 정렬함, .sort()는 리스트 객체만 정렬하고 sorted()는 모든 이터러블 객체 정렬

sorted_num_list = num_list.sort()
max_move = 0
for i in range(n):
    move = num_list[i][1] - i
    if move > max_move:
        max_move = move

print(max_move + 1)