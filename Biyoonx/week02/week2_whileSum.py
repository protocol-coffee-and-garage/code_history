import sys
read = sys.stdin.readline

while True:
    result = sum(map(int, read().split()))
    if result == 0:
        break
    print(result)