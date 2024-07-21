import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BackJ_1158 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Queue<Integer> q = new LinkedList<>();
        StringBuilder res = new StringBuilder();
        int n = Integer.parseInt(st.nextToken()); //n명
        int k = Integer.parseInt(st.nextToken()); //k번째 -제거

        for(int i = 1; i <= n; i++){
            q.add(i);
        }
        res.append("<");
        while (!q.isEmpty()) {
            for (int i = 1; i < k; i++) {
                q.add(q.poll());  //버린 카드  맨 뒤로
            }
           res.append(q.poll());
            if (!q.isEmpty()) {
                res.append(", ");
            }
        }
       res.append(">");

        System.out.println(res.toString());
    }
}
