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


