# week1 : Debugging, I/O, Basic Data Type and Data Structures

📌사용할 언어로 Python을 선택하였으나 중간에 자바 정보가 덧붙여질 수 있음

## Debugging

- 명령어 디버깅  
  [Python 공식 문서 - 디버깅 명령어(3)](https://docs.python.org/ko/3/library/pdb.html)  
  [Python 공식 문서 - 디버깅 명령어(3.9)](https://docs.python.org/ko/3.9/library/pdb.html)  
  [점프 투 파이썬 - 라이브러리 예제 편 17장 기타 서비스 다루기 110 만든 코드를 디버깅하려면? ― pdb](https://wikidocs.net/133085)  
  [<Python> 디버깅 도구 사용법(덕후가 되지 못한 이무기)](https://dmoogi.tistory.com/93)

- IDE 디버깅
  - VS Code : [파이썬 초보 탈출하기 #2 | 디버깅 Debugging(나도코딩)](https://www.youtube.com/watch?v=_1HM6MJMYPw)
  - IntelliJ : IDE 디버깅 툴 사용법에 가까운 듯 하여 「자바 잘 읽는 법」 참고

## I/O

- `input()` 대신 `sys.stdin.readline()`을 사용할 것  
  (속도 개선이 가능, 문제에 따라서는 `input()`으로 속도 문제를 겪을 수도 있음)
  - cf.Java에서 `Scanner`나 `System.out.println` 대신 `BufferedReader`가 권장됨
- `input()` : 내장함수. 사용자의 입력을 받은 후 개행문자(`\n`) 제거하고 문자열로 변환한 후 반환하는 과정을 거침. 입력 없을 때 에러(`EOFError`)
- `sys` : 라이브러리(`import sys` 필요). 사용자의 입력을 버퍼에 담아놨다가 요청시 전처리 없이 값을 읽어옴(문자열은 개행문자(`\n`) 포함 주의). 입력 없을 때 에러(`EOFError`)가 아니라 빈 문자열 반환.

  - 함수는 1급 객체이므로 변수에 담아 간편하게 사용 가능

  ```python
  import sys
  read = sys.stdin.readline
  num = int(read())
  ```

  - sys.stdin 개체 속성 보기

  ```python
  import sys
  dir(sys.stdin)
  ```

  - 개행문자(`\n`) 제거

  ```python
  import sys
  sys.stdin.readline().strip()
  ```

- 상황별 예시(문자열은 기본적으로 `int()` 없이 `strip()`을 추가)

  - 한 줄에 여러 개 숫자를 각 변수에 저장  
    1 2 3 4 5

  ```python
  import sys
  read = sys.stdin.readline
  a, b, c = map(int, read().split())
  ```

  - 한 줄에 여러 개 숫자를 리스트로 저장  
    1 2 3 4 5

  ```python
  import sys
  read = sys.stdin.readline
  num_list = list(map(int, read().split()))
  ```

  - 여러 줄에 여러 개 숫자를 리스트로 저장  
    5  
    1  
    2  
    3  
    4  
    5
    - 간단한 버전
    ```python
    import sys
    read = sys.stdin.readline
    line_num = int(read())
    num_list = [int(read()) for _ in range(line_num)]
    ```
    - `append()` 사용 버전
    ```python
    import sys
    read = sys.stdin.readline
    num_list = []
    line_num = int(read())
    for i in range(line_num):
        num_list.append(int(*read().split()))
    ```
  - 여러 줄에 여러 개 문자열 리스트로 저장  
    5  
    a  
    b  
    c  
    d  
    e
    - 간단한 버전
    ```python
    import sys
    read = sys.stdin.readline
    line_num = int(read())
    str_list = [read().strip() for _ in range(line_num)]
    ```
    - `append()` 사용 버전
    ```python
    import sys
    read = sys.stdin.readline
    str_list = []
    line_num = int(read())
    for i in range(line_num):
        str_list.append(*read().split())
    ```
  - 여러 줄에 여러 숫자 2차원 리스트로 저장(for 그래프)  
    3  
    1 2  
    3  
    4 5

  ```python
  import sys
  read = sys.stdin.readline
  line_num = int(read())
  matrix = [list(map(int, read().split())) for _ in range(line_num)]
  ```

- 출력 : `print()`를 사용하되 tuple의 경우 `*`를 통한 unpacking 활용

<br>

- 참고자료  
  [Python 코딩 테스트 : 입력(rookieand.log)](https://velog.io/@rookieand/1-Python-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%85%EC%B6%9C%EB%A0%A5)  
  [여러 줄을 한 번에 입력받고 싶을 때 : sys.stdin.readlines()와 공백 제거 : strip()(전자스컹크)](https://electroskunk.tistory.com/17)  
  [Python 코딩 테스트 : 출력(rookieand.log)](https://velog.io/@rookieand/2-Python-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%B6%9C%EB%A0%A5)

<br>

> - 파이썬 관련 코딩 팁✨  
>   [코테를 위한 파이썬 문법 - 1. 자료형(mildroast)](https://mildroast.tistory.com/16)  
>   [코테를 위한 파이썬 문법 - 6. 주요 라이브러리의 문법과 유의점(mildroast)](https://mildroast.tistory.com/23?category=949142)  
>   [Python3 코딩테스트 기초 TIP 모음(SJ_Koding)](https://sjkoding.tistory.com/18)

## Basic Data Type and Data Structures

- NoneType
  - None
  - 변수가 비어있음. 다른 언어에서의 null.
  - == 로 비교할 수 있으나 is를 활용하여 비교할 것 권장
- bool
  - True / False / bool(obj)
  - boolean 타입
  - True는 1, False는 0으로 취급
  - Falsy : False, None, 0, 0.0, 0L, 0j, "", [], (), {}
  - Truthy : Falsy한 값을 제외한 모든 obj
- int
  - 정수형, int(값)
- float

  - 실수형(소숫점 포함), float(값), e / E
  - 0.0001처럼 정수부분이 0인 경우 생략 가능(0.0001 == .0001)
  - inf라는 무한대를 표현할 수 있음(float("inf"), float("-inf"))
  - 부동소수점 문제가 있으나 `decimal`를 사용해 보다 정확한 연산 가능
  - e / E로 지수표현 가능(1e2 == 1E2 == 1 \* (10 \*\* 2) == 100.0)

  ```python
  import decimal
  float(decimal.Decimal('.1') + decimal.Decimal('.2')) # 0.3

  0.1 + 0.2 # 0.30000000000000004
  ```

- complex
  - 복소수. 허수부 뒤에 j를 붙여 표현, 또는 complex 함수 사용
  - 1 + 2j == complex(1, 2)
  - 실수 부분만 : (1 + 2j).real = 1.0
  - 허수 부분만 : (1 + 2j).imag = 2.0
- 시퀀스 자료형 : str, list, tuple, bytes, bytearray, range
  - 인덱싱, 슬라이싱 가능, in / not in로 포함/비포함 여부, +로 연결, *로 반복, 패킹 / 언패킹, *로 언패킹
  - str
    - 문자열, str(값)
    - immutable('string'[0] = 't' 불가)
    - lower() / upper() / find() / index() / count() / strip() / replace() / split() / join() / format() / isalnum() / isdigit() / isalpha() / isascii() / rjust() / ljust() / center() / zfill() / translate()
    ```python
    a = 'str'
    b = "str"
    c = '''s
    t
    r'''
    d = """s
    t
    r"""
    e = f'my name is {a}, and yours is {b}.'
    f = f'my name is {{{a}}}, and yours is {{{b}}}.' # my name is {str}, and yours is {str}.
    g = 'my name is {}, and yours is {}.'.format(a, b)
    h = 'my name is {0}, and yours is {1}.'.format(a, b)
    i = 'my name is {mine}, and yours is {yours}.'.format(mine=a, yours=b)
    j = 'my name is %s, and yours is %s.' % (a, b)
    ```
  - list
    - 리스트
    - 하나의 리스트에 다양한 타입 저장 가능
    - 각 원소에 값이 아니라 값에 대한 참조가 저장되는 형태
    - 동적 배열(배열 크기가 정해진 형태가 아니라 동적으로 메모리 공간 확보) - mutable([1, 2, 3][0] = 0 가능)
    - append() / clear() / copy() / count() / extend() / index() / insert() / pop() / remove() / reverse() / reversed() / sort() / sorted()
    ```python
    list1 = [1, 'a', 2.0, [True], (False)]
    list2 = list(1, 'a', 2.0, [True], (False))
    ```
  - tuple
    - 튜플
    - 단일 요소를 담을 때는 요소 뒤에 ,를 넣어야 튜플로 인식 가능(type((0.1,)) != type((0.1)) >> tuple != float)
    - immutable((1, 2, 3)[0] = 0 불가)
    - count() / index()
    ```python
    tuple1 = (1, 'a', 2.0, [True], (False))
    tuple2 = tuple(1, 'a', 2.0, [True], (False))
    ```
  - bytes
    - 바이트
    - 아스키코드로 구성된 문자열만 가능
    - b'value' / bytes(길이) / bytes(반복 가능한 객체) / bytes(바이트객체)
    - immutable
    ```python
    bytes1 = b'oh'
    ```
  - bytearray
    - 바이트 배열
    - bytearray() / bytearray(길이) / bytearray(반복 가능한 객체) / bytearray(바이트 객체)
    - 요소에 값을 할당할 때 정수만 할당, 문자를 넣고 싶으면 ASCII 코드를 반환하는 ord('문자') 사용하여 ASCII 코드 할당
    - mutable
    ```python
    bytearray1 = bytearray(b'oh')
    ```
- dict

  - 딕셔너리
  - 키는 immutable 자료형(문자열, 숫자 튜플 등) 사용 가능, 값은 다양한 값 사용 가능
  - 중복 키 사용 불가, 여러 번 사용시 최신 값이 이전의 값을 덮어씀 >> mutable
  - 딕셔너리[키] 형태로 요소 값에 접근 / 변경 / 추가 할당 가능 >> 동적 크기, mutable
  - 두 list를 짝 짓는 zip 함수와 dict를 활용하여 딕셔너리 생성 가능
  - clear() / copy() / fromkeys() / get() / items() / in / keys() / pop() / popitem() / setdefault() / update() / values()

  ```python
  dict1 = {'key1' : 'val1', 'key2' : 'val2', 'key3' : 'val3'}
  dict2 = dict([('key1', 'val1'), ('key2', 'val2'), ('key3', 'val3')])
  dict3 = dict(key1='val1', key2='val2', key3='val3')
  dict4 = dict(zip(['key1', 'key2', 'key3'], ['val1', 'val2', 'val3']))
  dict5 = dict.fromkeys(['key1', 'key2', 'key3'], None)

  dict5 = {"num_list" : [1, 2], 11 : 'eleven', ('a', 'b') : [0, 1], True : 1}
  ```

- set
  - 셋(집합)
  - 순서 없음, 중복값 불허(값을 여러 개 넣어도 한 번만 추가됨, 문자열 넣을 시 중복 문자 제거됨)
  - 합집합 set1 | set2
  - 교집합 set1 & set2
  - 차집합 set1 - set2
  - 대칭차집합 set1 ^ set2
  - set은 mutable, 원소는 immutable만 가능
  - add() / in / not in / clear() / copy() / remove() / discard() / pop() / difference(others) / difference_update(others) / intersection(others) / intersection_update(others) / isdisjoint(other) / issubset(other) / issuperset(other) / symmetric_difference(other) / symmetric_difference_update(other) / union(others)
  ```python
  set1 = {1, 2, 3}
  set2 = set(1, 2, 3)
  ```
- collections 모듈
  - deque
  - Counter
  - OrderedDict
- function / class
- 날짜와 시간 : datetime 패키지, dateutil 패키지, time 패키지
- ord(문자) : 유니코드 정수 반환 / chr(정수) : 유니코드 문자 반환

- 1급 객체 : 변수 또는 자료구조 안에 담을 수 있음, 매개변수로 전달 가능, 반환값으로 사용 가능

- 참고자료  
  [견고한 파이썬](https://www.books.weniv.co.kr/python/chapter00)  
  [데이터 사이언스 스쿨 - 2.15 파이썬에서 날짜와 시간 다루기](https://datascienceschool.net/01%20python/02.15%20%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C%20%EB%82%A0%EC%A7%9C%EC%99%80%20%EC%8B%9C%EA%B0%84%20%EB%8B%A4%EB%A3%A8%EA%B8%B0.html)  
  [파이썬(python) - 일급 객체(first-class citizen)(개발하는 중생)](https://tibetsandfox.tistory.com/8)  
  [파이썬에서의 Truthy Falsy(Morgenrøde)](https://ryanking13.github.io/2018/04/05/python-truthy-falsey.html)  
  [파이썬 코딩 도장 - 47.3 bytes, bytearray 사용하기](https://dojang.io/mod/page/view.php?id=2462)
