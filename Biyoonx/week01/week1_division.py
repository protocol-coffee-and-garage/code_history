import sys
read = sys.stdin.readline
def quotient(*num):
    if ','.join(map(str, num)).find(',0', 1) != -1:
        raise ZeroDivisionError()
    if num[0] == 0:
        return 0
    if len(num) == 1:
        return num[0]
    return quotient(*num[:(len(num) - 1)]) / num[len(num) - 1]

num_list = [*map(float, read().split())]

print(quotient(*num_list))

# 기존 답변
a, b = list(map(int, input().split()))
print(a / b)