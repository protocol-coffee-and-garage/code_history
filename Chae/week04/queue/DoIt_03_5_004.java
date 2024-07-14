import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class DoIt_03_5_004 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //연산 수
        PriorityQueue<Integer> q = new PriorityQueue<>((o1, o2) -> { //우선순위 큐
            // o1과 o2를 비교하여 우선순위를 결정
            // 반환 값이 양수이면 o1이 o2보다 우선순위가 낮음
            // 반환 값이 음수이면 o1이 o2보다 우선순위가 높음
            // 반환 값이 0이면 o1과 o2의 우선순위가 같음
            int first_abs = Math.abs(o1);  //절대값 만들기
            int second_abs = Math.abs(o2);
            if(first_abs == second_abs){ //절대값이 같을 때
                return o1 > o2 ? 1 : -1;    //o1 > o2 = 1 =>양수 o2가 음수이기 때문에 우선
            }else{
                return first_abs - second_abs; // 절대값 기준 정렬 o1>o2 => 양수 -> o2 우선 / o1<o2 => 음수 -> o1 우선
            }
        });
        for(int i = 0; i < n; i++){
            int req = Integer.parseInt(br.readLine()); //입력 값 하나씩 읽음
            if(req == 0 ){
                if(q.isEmpty()){ //큐가 비어있을 때 0 출력
                    System.out.println("0");
                }else{
                    System.out.println(q.poll()); //
                }
            }else {
                q.add(req);
            }
        }

    }
}
