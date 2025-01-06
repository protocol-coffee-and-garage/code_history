import sys
read = sys.stdin.readline

n, k = map(int, read().split())
a_list = [*map(int, read().split())]

# 기본 방식
'''
a_list.sort()
print(a_list[k-1])
'''

# 퀵 정렬
def swap(target_list, a, b):
		target_list[a], target_list[b] = target_list[b], target_list[a]

def partition(target_list, s, e):
		pivot = target_list[s]
		left = s + 1
		right = e

		if left == right:
				if pivot > target_list[right]:
						swap(a_list, s, e)
				return right

		while left <= right:
				while left < len(a_list) and pivot > target_list[left]:
						left += 1
				while right >= 0 and pivot < target_list[right]:
						right -= 1
				if left <= right and target_list[left] > target_list[right]:
						swap(a_list, left, right)
						left += 1
						right -= 1
		if target_list[right] <= pivot:
				swap(target_list, s, right)
		else: # target_list[right] > pivot
				target_list.insert(right, pivot)
				target_list.remove(pivot)
		return right

def quickSort(target_list, s, e):
		pivot_index = ''
		return 0