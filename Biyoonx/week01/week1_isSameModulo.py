import sys
read = sys.stdin.readline

a, b, c = map(int, read().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

# 기존 답변
a, b, c = list(map(int, input().split()))
# print()는 동일