import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.PriorityQueue;
import java.util.Stack;
import java.util.StringTokenizer;

public class BackJ_9012 {
    public static void main(String[] args) throws Exception{
        //여는 괄호 push -> 닫는 괄호가 있으면 poll

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //연산할 수

        boolean res = true;

        for (int i = 0; i < n; i++) {
            char[] cArr = br.readLine().toCharArray();
            Stack<Character> stack = new Stack<>();
            for (char c : cArr) {
                if (c == '(') {
                    stack.push(c);
                } else{    //")" 입력 시
                    if(stack.empty()){
                       stack.push(c);
                       break;
                    }else{
                        stack.pop();
                    }
                }
            }
            if (stack.empty()) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
