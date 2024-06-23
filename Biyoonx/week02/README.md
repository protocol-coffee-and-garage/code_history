# week2 : Array, List, Prefix Sum, Hash/Map

## Array / List
- 파이썬은 리스트가 배열 특성도 함께 가짐
- 동적 배열로 list에 들어가는 값의 자료형이나 list의 크기가 정해져 있지 않음
- 인덱스로 요소에 접근 가능

### 기본 특징
- 객체는 모두 heap 영역에 저장됨(파이썬의 변수는 객체(객체의 주소)를 가리킴)
- 선언된 자료형을 가리키는 강타입의 언어와 다르게 요소가 모두 참조값으로 구성됨(=타입과 크기가 동적)
- 단일 자료형(문자, 정수, 실수 등)을 사용한다면, array 모듈의 array 클래스를 이용할 수 있음

- 참고자료  
[좌충우돌, 파이썬으로 자료구조 구현하기 - 01장 파이썬의 변수는 객체에 붙인 이름표다.](https://wikidocs.net/189480)  
[좌충우돌, 파이썬으로 자료구조 구현하기 - 02장 파이썬은 리스트가 배열(array)을 대신한다.](https://wikidocs.net/189478)

(python에서의 특징 X)
#### 배열
- 메모리 연속 공간에 값이 채워져 있는 형태
	- 값을 추가/삭제하려면 주변 값을 이동시켜야 함
	- 크기를 바꿀 수 없음
- 인덱스를 통해 값 즉시 접근(O(1))
- 선언한 자료형 값만 저장 가능(ex.java ```String[]```)
#### 리스트
- 값과 포인터를 묶은 노드를 포인터로 연결한 구조
	- 노드로 연결하는 형태이므로 값의 추가/삭제가 쉬움
	- 크기를 바꿀 수 있음
	- 포인터 저장할 공간 필요
- 인덱스가 없어 값에 접근하려면 head에서부터 연결된 순서대로 접근(속도가 느림)

## Prefix Sum
- 부분함 인덱스 찾기([Subarray with given sum](https://www.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1))
1. 이중 반복문
```python
def find_sub_array(arr: list[int], s: int) -> list[int]:
    for i in range(len(arr)):
        sub_total: int = 0
        for j in range(i, len(arr)):
            sub_total += arr[j]
            if sub_total == s:
                return [i+1, j+1]
    return [-1]
```
2. 부분 합(포인터 2개)
```python
def find_sub_array(arr: list[int], s: int) -> list[int]:
    left: int = 0
    sub_total: int = 0
    for right in range(len(arr)):
        sub_total += arr[right]
        while left < right and sub_total > s:
            sub_total -= arr[left]
            left += 1
        if sub_total == s:
            return [left+1, right+1]
    return [-1]
```

[좌충우돌, 파이썬으로 자료구조 구현하기 - 02-04. 제시된 합을 가진 부분 배열 찾기](https://wikidocs.net/224917)

## Hash/Map
### hash
- 데이터를 고유한 값으로 변환하는 과정
- 해시 함수를 사용하여 데이터를 해시 값으로 변환하고, 이 해시 값을 통해 데이터를 저장하거나 검색
- 해시 함수에 의해 변환된 데이터는 보통 해시 테이블(hash table)이라는 배열에 저장
- 배열의 각 요소는 해시 값에 따라 인덱스화되어 저장
- 해시 테이블은 해시 충돌(hash collision)을 해결하기 위한 방법들이 존재
<img src="https://wikidocs.net/images/page/193049/ds-043.png"/>
- dictionary를 활용해 해시 함수로 연결되는 해시테이블을 만들 수 있음
- 객체의 해시값을 반환하는 hash() 함수 활용 가능  
[Python 공식 문서 내장 함수 - hash(obj)](https://docs.python.org/ko/dev/library/functions.html#hash)
### map
- 키-값 쌍을 저장하고 이를 검색하기 위한 자료 구조
- 해시 테이블을 기반으로 구현되기도 하지만, 맵 자체는 키-값 쌍을 저장하는 개념적 자료 구조
- python에서는 dictionary로 구현되어 있음

- 참고자료  
[좌충우돌, 파이썬으로 자료구조 구현하기 - 06장 파이썬으로 해시 테이블 구현하기](https://wikidocs.net/193049)