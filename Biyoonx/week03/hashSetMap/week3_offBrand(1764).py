import sys
read = sys.stdin.readline

n, m = map(int, read().split())
unheardPeople = [read().strip() for _ in range(n)]
unseenPeople = dict.fromkeys([read().strip() for _ in range(m)], True)

unknownPeople = []
for person in unheardPeople:
		if person in unseenPeople:
				unknownPeople.append(person)
unknownPeople.sort()

print(len(unknownPeople))
print('\n'.join(unknownPeople))