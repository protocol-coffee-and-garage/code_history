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

### 자료형

-

### 자료구조

-
