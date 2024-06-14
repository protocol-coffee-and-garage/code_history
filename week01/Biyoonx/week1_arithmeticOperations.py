import sys
from functools import reduce
read = sys.stdin.readline

def difference(num):
    return num[0] - sum(num[1:])
def product(num):
    if ','.join(map(str, num)).find(',0', 1) != -1:
        return 0
    return reduce(lambda x, y: x * y, num)
def quotient(num):
    if ','.join(map(str, num)).find(',0', 1) != -1:
        raise ZeroDivisionError()
    if num[0] == 0:
        return 0
    if len(num) == 1:
        return num[0]
    return reduce(lambda x, y: x // y, num)
def remainder(num):
    if ','.join(map(str, num)).find(',0', 1) != -1:
        raise ZeroDivisionError()
    if num[0] == 0:
        return 0
    if len(num) == 1:
        return num[0]
    return reduce(lambda x, y: x % y, num)
num_list = [*map(float, read().split())]

print(int(sum(num_list)))
print(int(difference(num_list)))
print(int(product(num_list)))
print(int(quotient(num_list)))
print(int(remainder(num_list)))

# 기존 답변
a, b = list(map(int, input().split()))
print(a + b)
print(a - b)
print(a * b)
print(int(a / b))
print(a % b)