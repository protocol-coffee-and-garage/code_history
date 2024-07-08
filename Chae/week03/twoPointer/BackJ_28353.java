import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BackJ_28353 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken()); //고양이 수
        int k = Integer.parseInt(st.nextToken()); //최대 무게

        st = new StringTokenizer(bf.readLine());
        int arr[] = new int[n];

        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken()); //고양이 배열
        }

        Arrays.sort(arr);

        int cnt = 0;

        for(int i = 0; i < n; i++){
            int j = i+1;
            int sum = arr[i]+arr[j];
            if(sum <= k){
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
