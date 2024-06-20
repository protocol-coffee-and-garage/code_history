import sys
read = sys.stdin.readline
print(sum(map(int, read().split())))
# 이렇게 하면 A+B뿐만 아니라 인자가 3개 이상이어도 계산되는데 괜찮을까?

# 기존 답변(이게 더 빠름......?!)
a, b = list(map(int, input().split()))
print(a + b)