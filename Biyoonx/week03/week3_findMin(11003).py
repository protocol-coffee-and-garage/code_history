from collections import deque
import sys
write = sys.stdout.write

read = sys.stdin.readline
n, l = map(int, read().split())
a_list = list(map(int, read().split()))

# read = sys.stdin.read
# read_data = read().split()
# n, l = int(read_data[0]), int(read_data[1])
# a_list = list(map(int, read_data[2:]))

dq = deque()
# result = []
for idx in range(n):
    while dq and (dq[-1][1] > a_list[idx]):
        dq.pop()
    dq.append((idx, a_list[idx]))
    if dq[0][0] <= idx - l:
        dq.popleft()
    write(f'{dq[0][1]} ') # print(dq[0][1], end=' ')
    # result.append(dq[0][1])

# write(' '.join(map(str, result)))
# result에 담아서 출력하니 메모리 초과 문제가 발생하여 리스트에 담아두지 않고 결과를 바로 출력하도록 함
# read = sys.stdin.read + a_list = [*map(int, read().split())] 조합일 때 메모리 초과가 남