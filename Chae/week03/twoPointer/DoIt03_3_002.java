import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class DoIt03_3_002 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine()); //재료의 개수
        int m = Integer.parseInt(bf.readLine());  //합해서 만들 값
        int[] a = new int[n];  //재료들
        StringTokenizer st = new StringTokenizer(bf.readLine());

        for(int i = 0; i < n; i++){
            a[i] = Integer.parseInt(st.nextToken());  //재료들 배열에 넣기
        }
        Arrays.sort(a);  //배열 오름차순 정렬
        int count = 0;
        int i = 0;    //start
        int j = n-1; //인덱스 0부터라서 //end

        while (i < j) {
            if (a[i] + a[j] < m) {  //합이 m보다 작을 때, start수를 올림
                i++;
            } else if (a[i] + a[j] > m) { //합이 m보다 클 때, end를 내림
                j--;
            } else {  //같을 때 개수 셈
                count++;
                i++;    //i,j중 하나만 올리거나 내렸을 때 어차피 m보다 합이 작을 때/클 때 경우를 지나서 두 개 다 옮기게 됨.
                j--;
            }
        }
        System.out.println(count);
        bf.close();
    }
}
