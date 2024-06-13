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
  실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답
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

