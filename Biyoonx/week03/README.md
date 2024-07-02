# week3 : Two Pointer, Sliding Window, Set

## Two Pointer
- 두 개의 포인터의 위치를 기록하면서 처리하는 알고리즘
- 정렬된 두 리스트 합집합에도 사용(두 개의 포인터이므로!)
- 연산 횟수의 최댓값이 커서 O(n*log*n)도 제한 시간을 초과할 때 사용하기 좋은 O(n)의 알고리즘
- 두 포인터의 범위 또는 두 개의 값과 관련된 연산에서 사용
- 시작 포인터는 항상 끝 포인터보다 작거나 같아야 함(start <= end)
- 시작 포인터의 끝 포인터가 동일할 경우 아무것도 포함하지 않는 부분 배열 의미
- 각 포인터는 탐색 범위의 시작과 끝 or 시점에 따라 포인터 이동(한쪽 고정 or 양쪽 이동)

## Sliding Window
- 고정 길이 슬라이딩 윈도우 : 윈도우(구간)의 크기를 일정하게 유지하면서 배열/리스트 탐색
- 가변 길이 슬라이딩 윈도우 : 필요에 따라 윈도우(구간)의 크기를 변경하면서 배열/리스트 탐색
- 일정한 구간을 가지고 구간 이동하면서 배열/리스트를 훑는 알고리즘이라는 설명도 많음

- 참고자료  
[[Algorithm] 투포인터(Two Pointer) 알고리즘 - Butter Shower](https://butter-shower.tistory.com/226)  
[투포인터 알고리즘.md - WooVictory](https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.md)  
[[Java/알고리즘] 투 포인터 알고리즘(Two Pointer Algorithm) 이해하기 -1 : 종류, 활용방안 - Contributor9](https://adjh54.tistory.com/384)

## Set
- 중복 없음, 순서 없음
- Set을 생성하려면 set(iterable한 값) e.g.문자열, 리스트, 튜플 등
- Set의 요소를 표현할 때는 {}를 사용하지만 빈 집합을 {}로 생성할 수는 없음. 딕셔너리와 동일한 표현이므로 {}만 사용하면 빈 딕셔너리가 생성됨. 값이 있을 때 딕셔너리는 {키: 값}의 형태고 Set은 {값}의 형태.
- 저장된 값을 인덱싱으로 접근하려면 튜플/리스트로 변환 후 가능
- 교집합, 합집합, 차집합 구할 시 유용
	- 교집합
	'''python
	set1 & set2
	set1.intersection(set2)
	'''
	- 합집합
	'''python
	set1 | set2
	set1.union(set2)
	'''
	- 차집합
	'''python
	set1 - set2
	set1.difference(set2)
	'''
- 관련 함수 : add / update /remove

- 참고자료  
	[점프 투 파이썬 - 02-6 집합 자료형](https://wikidocs.net/1015)

- 문제풀이 참고자료
	- 1253 좋다  
	[[백준 / BOJ] 1253 좋다 - JJUN_0](https://dlwnsdud205.tistory.com/158)