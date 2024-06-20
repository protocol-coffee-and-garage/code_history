import sys
read = sys.stdin.readline

def oven_clock(h:int, m:int, t:int):
		return f'{(h + (m + t) // 60) % 24} {(m + t) % 60}'

hour, minute = map(int, read().split())
time = int(read())

print(oven_clock(hour, minute, time))