import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class DoIt_03_5_002 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine()); //수열 개수
        int[]a = new int[n]; //수열
        int[]ans = new int[n]; //정답 배열
        String[] str = bf.readLine().split(" ");
        for(int i = 0; i < n; i++){
            a[i] = Integer.parseInt(str[i]);  //수열 만들기

        }
        Stack<Integer> stack = new Stack<>();
        stack.push(0);  //스택에 인덱스 값 넣기

        for(int i = 1; i < n; i++){ //수열[0]의 오른쪽부터 확인 => 1부터 시작
            while (!stack.isEmpty() && a[stack.peek()] < a[i]){ //  ex)a[0] < a[1] => 오큰수 존재
                ans[stack.pop()] = a[i];   //ans[0]에 a[1] 값 넣기
            }
            stack.push(i);  //다음 인덱스 넣기
        }
        while(!stack.empty()){
            ans[stack.pop()] = -1; //없으면 정답 인덱스에 -1
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(int i = 0; i < n; i++){
            bw.write(ans[i] + " ");
        }
        bw.write("\n");
        bw.flush();
    }
}
