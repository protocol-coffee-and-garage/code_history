# week4: Stack, Queue, Deque

> 풀어야 할 것  
> 2차원 배열 : 색종이(2563)  
> 투 포인터 : 수열(2559), 최솟값 찾기(11003)

## Stack

- 삽입과 삭제 연산이 후입선출로 이뤄지는 자료구조
- 삽입과 삭제가 한 쪽에서만 일어남(ex.프링글스)
- top : 삽입과 삭제가 일어나는 위치(출입구 바로 앞에 있는 값)
- append(push) / pop / peek
- DFS, 백트레킹 문제와 연관 多
- 후입선출은 재귀 함수 알고리즘 원리와 일맥상통?
  <img src="https://inblog.ai/_next/image?url=https%3A%2F%2Fwww.notion.so%2Fimage%2Fhttps%253A%252F%252Fs3-us-west-2.amazonaws.com%252Fsecure.notion-static.com%252Fd7421e6c-f9f1-489f-82c2-5d1590daaa93%252FUntitled.png%3Ftable%3Dblock%26id%3Deba9b97b-de49-4cf6-bd1e-d13e43900fb0%26cache%3Dv2&w=2048&q=75"/>
- 이미지 출처 : [[자료구조] Stack & Queue - 백엔드블로그-dohyeong](https://inblog.ai/dohyeong/stack-queue-1514)

## Queue

- 삽입과 삭제 연산이 선입선출로 이뤄지는 자료구조
- 삽입과 삭제가 양방향에서 일어남(ex.대기열, 파이프)
- rear : 큐에서 가장 끝 데이터를 가리키는 영역(최근에 삽입된 값이 있는 위치)
- front : 큐에서 가장 앞의 데이터를 가리키는 영역(삭제될 값이 있는 위치, 삽입된 값 중 가장 오래된 값)
- 파이썬에서는 collections.deque를 보통 활용
- 선형 / 원형(환형), 우선순위 큐, 데크
- BFS 문제와 연관 多
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F5NOv1%2FbtqSTINnoq8%2F4f8bjzzf6W4POewlq8At31%2Fimg.png"/>
- 이미지 출처 : [[자료구조] 큐 (Queue) - yoongrammer](https://yoongrammer.tistory.com/46)

## Deque

- 양방향 큐
- 이중연결 리스트로 구현
- append(item) / appendleft(item) / pop() / popleft() / extend(array) / extendleft(array) / remove(item)(제일 처음 나온 해당 string만 제거됨) / clear() / reverse() / rotate(num)(데크를 num만큼 회전, 양수면 오른쪽, 음수면 왼쪽)
- 참고 : [deque는 무엇인가? - harper9808.log](https://velog.io/@harper9808/deque%EB%8A%94-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)

## Priority Queue VS Heap

- PriorityQueue 클래스가 heapq 모듈 이용
- PriorityQueue, heapq 모두 기본적으로 최소힙(최대합으로 만들기 위해서는 부호변경)
- PriorityQueue에서는 정렬순서를 지정할 수 있음(값을 넣는 put 메서드를 쓸 때 튜플로 넣되 (정렬순서, 값) 형식으로 넣을 것)
- PriorityQueue - Thread-Safe
- heapq - Thread-Non-Safe, 실행 시간이 더 빠름
  > 우선순위 큐 : 각 요소가 우선순위를 가지며, 높은 우선 순위를 가진 요소가 먼저 제거되는 데이터 구조  
  > 힙 : 완전 이진 트리의 형태를 가지며, 힙 속성을 만족하는 데이터 구조, 우선순위 큐를 구현하는 데 사용하는 일반적 방법  
  > _힙 속성 : 힙 데이터 구조에서 모든 노드가 특정 규칙을 만족해야 하는 성질(eg.최대 힙 속성, 최소 힙 속성 등)_
- 참고자료  
  [파이썬의 우선순위 큐(PriorityQueue) 사용법 - DaleSeo](https://www.daleseo.com/python-priority-queue/)  
  [파이썬의 heapq 모듈로 힙 자료구조 사용하기 - DaleSeo](https://www.daleseo.com/python-heapq/)
