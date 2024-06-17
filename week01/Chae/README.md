# code_history

### git 사용법

```
git status → 현재 상태 보기
git pull origin main 
git add -A 또는 git add .  → 모든 수정 사항 올리기
git commit -m “커밋메세지” → 커밋
git push  → 레포지토리에 올리기

pull -> commit -> pull -> push
```

### Debugging

```
step over: 다음 라인 실행
step into: 현재 메소드(실행중인 메소드 라인) 확인
            UserService userDao.save()-> step into -> UserDao의 save() 메서드로 이동
step out: 메서드를 호출한 곳으로 돌아옴
            UserService userDao.save()-> step into -> UserDao의 save() -> step out -> UserService userDao.save()
resume program: 다음 breakpoint까지 실행
Evaluate: 코드나 메서드 실행해서 result 볼 수 있음

```
### 자바 자료형

기본 자료형
```
Boolean: 8비트 true/false
short:16비트 -32,768 ~ +32,767
int: 32비트 -2,147,483,638~+2,147,483,647
long: 64비트 -9223372036854775808~+9223372036854775807
float: 32비트 -3.402932347e+38~+3.40292347e+38
double: 64비트 -179769313486231570e+308~1.79769313486231570e+08
char: 16비트 –128~127

Long보다 큰 값을 사용해야 할 때
BigInteger: 문자열 형태로 담을 수 있어서 범위 무한
```

참조 자료형 (Collection Framework)

- List: 중복O, 순서O
```
  - ArrayList: 가변크기 Array로 구성된 리스트
  - ListIterator: List에 Iterator사용, 양방향으로 객체 탐색이 가능
  - LinkedList: 자료의 주소값을 연결, 삽입/삭제 용이, 순차접근 방식으로 탐색은 ArrayList가 나음
  - Vector: 기본적으로 ArrayList와 동일하지만 잘 사용하지 않음
     - Stack
```
<img width="734" alt="스크린샷 2024-06-18 오전 8 31 37" src="https://github.com/protocol-coffee-and-garage/code_history/assets/121208913/24122ed1-cdb4-43ec-b53b-ca5ce3b73c39">

- Set: 중복X, 순서X
```
SortedSet: 오름차순 정렬 저장
TreeSet: 오름차순 정렬, 트리형태 저장
HashSet: 키+값을 가진 해시테이블 사용, 정렬X
```

- Map: 키+값 (키: 중복X, 값: 중복O)
```
  - HashMap<K, V>: key와 value를 묶어 하나의 entry로 저장, 검색속도 빠름
  - TreeMap<K, V>: key와 value 데이터를 이진 검색 트리의 형태로 저장, 추가/삭제 빠름




참고: https://www.devkuma.com/docs/java/collection-framework/



###입출력 
- A, B 입력 받아 A+B 출력
```
import java.util.*;
class Main {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        int A, B;
        A = sc.nextInt();
        B = sc.nextInt();
        System.out.println(A+B);
    }
}
```
-  A, B 입력 받아 A/B 출력
  실제 정답과 출력값의 **절대오차 또는 상대오차가 10-9 이하**이면 정답
```
import java.util.*;
public class Main {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        Double A = sc.nextDouble();
        Double B = sc.nextDouble();
        System.out.println(A/B);
    }
}
```
- 입력 받은 문자열에 ??! 추가
```
import java.util.*;
class Main {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        String A = sc.nextLine();
        System.out.println(A+"??!");
    }
}
```
- 불기 -> 서기 전환
```
import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int y = sc.nextInt();
        System.out.println(y - 543);
    }
}
```

