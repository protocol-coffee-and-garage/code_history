import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class DoIt_03_5_003 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        int n = sc.nextInt(); //카드 개수
        for(int i = 1; i <= n; i++){ //1부터 시작해서 개수까지
            q.add(i);   //1~n 카드 큐
        }
        while (q.size() > 1){ //1장 남을 때까지 반복
            q.poll();  //맨 앞 카드 버리기
            q.add(q.poll());  //버린 카드 바로 다음 카드를 맨 뒤로

        }
        System.out.println(q.poll());  //마지막 한 장 값
    }
}
