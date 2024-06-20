import sys
read = sys.stdin.readline

num1, num2 = [read().strip() for _ in range(2)]

for char in num2[::-1]:
    print(int(num1) * int(char))
print(int(num1) * int(num2))

# print() 함수는 아래처럼 제너레이터 표현식 직접 처리 불가
# print(f'{int(num1) * int(idx)}\n' for idx in num2)

# 기존 답변
n1 = int(input())
n2 = list(map(int, input()))
for n in reversed(n2):
    print(n1 * n)
print(n1 * int(''.join(map(str, n2))))

# 참고 답변
results = [f'{int(num1) * int(char)}' for char in num2[::-1]]
print('\n'.join(results))
print(int(num1) * int(num2))