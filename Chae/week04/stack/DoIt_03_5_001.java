import java.util.Scanner;
import java.util.Stack;
import java.util.*;

/*BackJ_1874*/
public class DoIt_03_5_001 {
    public static void main(String[] args) {


        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); //수열 개수
        int[] a = new int[n];  //받은 자연수로 수열 만들기
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack<>();

        StringBuffer bf = new StringBuffer();

        int num = 1; //stack에 들어가는건 자연수 오름차순
        boolean rs = true;

        for (int i = 0; i < a.length; i++ ){
            int su = a[i];  //수열의 수
            if(su >= num){ //수열 값이 자연수보다 크면 -> 수열 값까지 push
                while(su >= num){
                    stack.push(num++);
                    bf.append("+\n"); //push = "+" 입력하고 줄바꿈
                }
                stack.pop();   //수열 값 == 자연수 -> pop
                bf.append("-\n");   //pop = "+" 입력하고 줄바꿈
            }else{   //수열 값 < 자연수
                int t = stack.pop();

                if(t < su){
                    System.out.println("NO");
                    rs = false;
                    break;
                }else{
                    bf.append("-\n");
                }

            }
        }

    if(rs){
        System.out.println(bf.toString());
    }

    }
}

