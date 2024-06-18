# week1 : 디버깅, I/O, 기본 데이터 유형 및 데이터 구조
사용 언어: Java

### 디버깅(Debugging)👾

Java 디버깅 방법
프로그램 오류를 찾아내고 수정하여 예상대로 작동하도록 만드는 필수 과정
```
step1. 브레이크 포인트 설정
step2. 단계별 실행
step3. 변수값 확인 및 수정
step4. 콘솔 사용
```
<br/> **1. 명령어 기반 디버깅**  
- 자바 디버그 인터페이스(JDI)를 사용하는 **jdb[^1]** 명령어를 통해 수행   
- 리눅스 터미널, 윈도우 명령프롬프트(cmd)에서 가능  
[^1]: jdb(Java Debugger): 자바 디버거. 명령줄 인터페이스를 통해 수행
```
 `javac 파일명.java`       : 프로그램을 파일로 저장 후 컴파일
 `jdb 클래스명`            : 프로그램을 디버깅 모드로 시작
 `stop at 클래스명:라인번호`: 라인번호에 브레이크 포인트 설정
 `run`                     : 프로그램 실행
 `step`                    : (=Step Into)다음 명령으로 이동
 `next`                    : (=Step Over)다음 명령으로 이동
 `print 변수`              : 변수의 현재 값 출력
 ```  
  
<br/> **2. 개발환경(IDE)에서의 디버깅GUI)**
 - 브레이크 포인트, 변수확인, 스택 트레이스 등 모든 작업을 그래픽 인터페이스로 수행 가능
 - 직관적, 쉽게 사용 가능하여 초보자에게 적합
 - 대표적 IDE로는 Eclpise, IntelliJ, NetBeans

```
< 단축키 >
(F11): 디버그모드 진입
(F5) : (=Step Into) 현재 줄을 실행 > 함수 내부로 진입
(F6) : (=Step Over) 현재 줄을 실행 > 다음줄 이동
(F7) : (=Step Out)  메소드 단위 이동 (현재 함수 실행 > 호출 함수로 돌아감)
(F8) : 다음 브레이크 포인트로 이동
```


<br/> **번외. 개발자도구 디버깅(=브라우저 디버깅)**
- 웹 브라우저에서 제공하는 개발자 도구를 사용하여 웹 애플리케이션의 디버깅 작업 수행
- JavaScript 디버깅, DOM 탐색 및 조작(Html), css 수정 및 문제 해결, 네트워크 요청 추적, 콘솔 포함

<br/>  

> [!NOTE]
> [Java] 이클립스 디버깅하기!  
> https://dpdpwl.tistory.com/62  
>  
> [생활코딩] JAVA1 - 10.디버거  
> https://www.youtube.com/watch?v=nUSJaO4khdc  
>  
> [드림코딩] 코딩의 시작과 끝, 디버깅|실력있는 개발자의 필수 무기  
> https://www.youtube.com/watch?v=IwC-BVM2_YQ

# 
### 입출력(I/O)
Java 입출력 방법  
<br/> **1. 표준입출력(콘솔입출력)**  
- 입력: Scanner 클래스 사용 
- 출력: System 클래스 사용 
```
 System.out.println : 줄바꿈 O 
 System.out.print   : 줄바꿈 X
 System.out.printf  : 포맷 지정 출력
```
> [!TIP]  
> 데이터를 하나씩 읽어오는 방식으로 속도 느린 편

<br/> **2. 파일입출력**  
키보드의 입력이 있을 때 마다 한문자씩 묶어 버퍼로 전송하여 모아서 한번에 프로그램에 전달  
- 입력(파일 읽기): FileReader, BuffreredReader 사용 
- 출력(파일 쓰기): FileWriter, BufferedWriter 사용  

   - bufferedReader/Writer는 버퍼를 사용하여 읽기와 쓰기를 하는 함수  
   - Buffer에 있는 IO 클래스인데, 데이터를 하나씩 읽어오는 방식이 아닌 임시공간(버퍼)에 저장해 두었다가 한번에 출력 및 전달하는 방식
 
> [!TIP]
> scanner 는 bufferedReader 보다 상당히 느림  
>   
> StringBuilder와 StringBuffer는 자바의 입출력(I/O) 방법에 직접적 포함 X 단순히 문자열을 다루는 클래스   

> [!NOTE]
> 백준 Hello World - JAVA  
> https://st-lab.tistory.com/2  
>  
> [Java] 빠른 입출력을 위한 BufferedReader, BufferedWriter, StringTokenizer, StringBuilder  
> https://rlakuku-program.tistory.com/33  

# 
### 기본 데이터 유형 및 데이터 구조(Basic Data Type and Data Structures)
Java 자료형 및 자료구조  

![자료형](https://github.com/protocol-coffee-and-garage/code_history/assets/108244671/52ba966b-42cf-4416-ab09-874421536fbf)

<br/>**1. 기본자료형(Primitive Data Type)**  
: 데이터를 저장하기 위해 사용되는 자료형을 의미함며 변수에 '실제 값'을 가짐   
- 기본자료형 
  - 정수형(Integer)   
     - byte : 8비트 정수(-128 ~ 127)  
     - short : 16비트 정수(-32,768 ~ 32,767)  
     - int : 32비트 정수  
     - long : 64비트 정수  
  - 실수형  
    - float : 32비트 부동소수점  
    - double : 64비트 부동소수점  
  - 문자형(Character)  
    - char : 16비트 유니코드 문자    
  - 논리형(Boolean)  
    - boolean: 참(true) 또는 거짓(false)    
 
<br/>**2. 참조자료형(Reference Data Type)**  
: 실제 값이 아닌 데이터가 저장된 '메모리 주소 값'을 가짐. 해당 값은 객체를 참조하는 변수 타입을 의미  
- 대표적인 참조자료형 종류   
  - 문자열(String)  
    - 문자열을 저장하는 클래스    
  - 배열(ArrayList)   
    - 동일한 타입의 데이터 여러개를 나타내는 클래스
  - 클래스(Class)  
    - 사용자 정의 데이터 타입을 나타내는 클래스  
  - 인터페이스(Interface)  
    - 메서드의 집합을 정의하는 인터페이스   
  - HashMap 키-값 쌍을 저장하는 클래스  
  - Queue 큐를 나타내는 인터페이스  
  - Stack 스택을 나타내는 인터페이스   

  
<br/>**※ 기본자료형 VS 참조자료형**    
<br/>![기본자료형vs 참조자료형](https://github.com/protocol-coffee-and-garage/code_history/assets/108244671/2e0a961d-7665-47eb-9fdd-7c41373258bb)


> [!NOTE]
> [Java] 자료형(Data Type) 이해하기: 기본 / 참조 자료형, 래퍼 클래스  
> https://adjh54.tistory.com/119
>
> Java 기본 특징 및 문법(데이터 타입)  
> https://velog.io/@fever-max/Java-%EA%B8%B0%EB%B3%B8-%ED%8A%B9%EC%A7%95-%EB%B0%8F-%EB%AC%B8%EB%B2%95-%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85
