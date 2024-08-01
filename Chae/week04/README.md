# code_history

### 스택 (Stack)
```
LIFO (Last In, First Out): 마지막에 삽입된 요소가 가장 먼저 삭제

- push: 스택의 맨 위에 요소를 추가.
- pop: 스택의 맨 위 요소를 제거하고 반환.
- peek: 스택의 맨 위 요소를 제거하지 않고 반환.
- isEmpty: 스택이 비어있는지 확인.
- size: 스택의 크기를 반환.
```

### 큐 (Queue)
```
FIFO (First In, First Out): 먼저 삽입된 요소가 가장 먼저 삭제 (선입선출)

- offer: 큐의 맨 뒤에 요소를 추가.
- poll: 큐의 맨 앞 요소를 제거하고 반환.
- peek: 큐의 맨 앞 요소를 제거하지 않고 반환.
- isEmpty: 큐가 비어있는지 확인.
- size: 큐의 크기를 반환.
```

### 우선순위 큐 (Priority Queue)
```
우선순위가 높은 요소가 먼저 처리되는 큐.

- offer: 우선순위 큐에 요소를 추가.
- poll: 우선순위가 가장 높은 요소를 제거하고 반환.
- peek: 우선순위가 가장 높은 요소를 제거하지 않고 반환.
- isEmpty: 우선순위 큐가 비어있는지 확인.
- size: 우선순위 큐의 크기를 반환.

 PriorityQueue<Integer> q = new PriorityQueue<>((o1, o2) -> {
            // o1과 o2를 비교하여 우선순위를 결정합니다.
            // 반환 값이 양수이면 o1이 o2보다 우선순위가 낮음
            // 반환 값이 음수이면 o1이 o2보다 우선순위가 높음
            // 반환 값이 0이면 o1과 o2의 우선순위가 같음
            return o1 - o2; // 오름차순 정렬
            // return o2 - o1; // 내림차순 정렬
        });
```

### Deque(Double Ended Queue)
```
양쪽 끝에서 삽입과 삭제가 모두 가능, 주로 ArrayDeque나 LinkedList 사용

삽입
- addFirst(E e): 요소를 덱의 앞에 추가.
- addLast(E e): 요소를 덱의 뒤에 추가.
- offerFirst(E e): 요소를 덱의 앞에 추가하고, 성공하면 true를 반환.
- offerLast(E e): 요소를 덱의 뒤에 추가하고, 성공하면 true를 반환.

삭제
- removeFirst(): 덱의 앞에서 요소를 제거하고 반환.
- removeLast(): 덱의 뒤에서 요소를 제거하고 반환.
- pollFirst(): 덱의 앞에서 요소를 제거하고 반환. 덱이 비어 있으면 null을 반환.
- pollLast(): 덱의 뒤에서 요소를 제거하고 반환. 덱이 비어 있으면 null을 반환.

조회
- getFirst(): 덱의 첫 번째 요소를 반환. 덱이 비어 있으면 예외를 발생.
- getLast(): 덱의 마지막 요소를 반환. 덱이 비어 있으면 예외를 발생.
- peekFirst(): 덱의 첫 번째 요소를 반환. 덱이 비어 있으면 null을 반환.
- peekLast(): 덱의 마지막 요소를 반환. 덱이 비어 있으면 null을 반환.

기타
isEmpty(): 덱이 비어 있는지 확인.
size(): 덱의 크기를 반환.
```
