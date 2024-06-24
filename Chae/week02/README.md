# code_history


## 해시
```
키(임의의 데이터) -> 해시 함수 -> 값(고정된 길이의 값)
- 값이 인덱스 순서대로 저장되는 것은 아님 -> 저장공간 많이 필요함
- 다른 값이지만 해시 함수 통과하면 같은 값이 나올 수 있음 -> 충돌 막기 위해 별도의 자료구조 필요
```

### 해시테이블
```
인덱스-키-값을 저장함

- 버킷: 하나의 버킷에 여러 개의 슬롯이 있음
- 슬롯: 하나의 레코드를 저장
```

## 맵
```
- key - Value는 중복될 수 있지만, Key는 고유한 값
```

### 트리맵
```
//키를 기준으로 정렬된 상태로 유지하는 맵

        // TreeMap 생성
        Map<String, Integer> treeMap = new TreeMap<>();

        // 값 추가
        treeMap.put("키", 값);
       
        // 값 가져오기
        treeMap.get("키")); 

        // 순회 (정렬된 순서대로 출력)
        for (Map.Entry<String, Integer> entry : treeMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());

```

### 해시맵

```
        // HashMap 생성
        Map<String, Integer> hashMap = new HashMap<>();

        // 데이터 추가
        hashMap.put();

        // 데이터 조회
        hashMap.get()); 

        // 데이터 수정
        hashMap.put("키", 값); 

        // 데이터 삭제
        hashMap.remove(키); 

        // 순회
        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            System.out.println("Key: " +entry.getKey() + ", Value: " + entry.getValue());

        // 순회(Iterator)
        Iterator<Entry<String, Integer>> it = hashMap.entrySet().Iterator();
        it.hasNext(); //읽을 요소 있으면 true
        it.next(); //다음 요소 읽기
        it.remove(); //다음 요소 삭제
        
        //예)
        while(it.hasNext()){
            Entry<String, Integer> entry = it.next();
            System.out.print(entry); //key-value 가져오기
	        System.out.println(entry.getKey()); //key만 가져오기
	        System.out.println(entry.getValue()); //Value만 가져오기
        }
        
        // 모든 키 반환
        for(String key : hashMap.keySet()){
            System.out.println(key);
        }
        
        // 모든 값 반환
        hashMap.values();
        
        
```