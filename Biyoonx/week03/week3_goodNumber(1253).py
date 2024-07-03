import sys
read = sys.stdin.readline

n = int(read())
num_list = [*map(int, read().split())]

# 시간초과
'''
num_list.sort()
result = 0
for idx in range(2, n):
    num = num_list[idx]
    for s in range(idx):
        diff = num - num_list[s]
        if diff == 0:
            continue
        if diff in num_list[s + 1:]:
            result += 1
            break
print(result)
'''

# 어디서부터 문제지......3 / 0 1 1 할 차례
result = 0
for idx in range(n):
    num = num_list[idx]
    s = 0
    e = n - 1
    while s < e:
        sub_sum = num_list[s] + num_list[e]
        print(f'num {num} sub_sum {sub_sum} s {s} e {e} result {result}')
        if sub_sum == num and (idx != s and idx != e):
            result += 1
            break
        elif sub_sum <= num or s == idx:
            s += 1
        else: # sub_sum > num or e == idx
            e -= 1

print(result)
