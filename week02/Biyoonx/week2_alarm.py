import sys
read = sys.stdin.readline

def alarm(h:int, m:int):
		if (m >= 45):
				return f'{h} {m - 45}'
		else:
				return f'{(h - 1) if (h > 0) else 23} {(60 + m) - 45}'

hour, minute = map(int, read().split())
print(alarm(hour, minute))