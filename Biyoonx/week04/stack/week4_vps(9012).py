import sys
read = sys.stdin.readline

t = int(read())
vps_appl = [read().strip() for _ in range(t)]

def isVps(str):
		ps = ['(', ')']
		stack = []

		for s in str:
				if s == ps[0]:
						stack.append(ps[0])
				elif s == ps[1]:
						if not stack:
								return 'NO'
						stack.pop()
      
		if stack:
				return 'NO'
  
		return 'YES'

result = [*map(lambda x: isVps(x), vps_appl)]
print('\n'.join(result))