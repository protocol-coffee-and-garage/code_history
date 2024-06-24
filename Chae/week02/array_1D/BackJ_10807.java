import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BackJ_10807 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine()); //개수
        StringTokenizer st = new StringTokenizer(bf.readLine()); // 정수들
        int v = Integer.parseInt(bf.readLine()); //주어진 정수

        int cnt = 0;

        for( int i = 0; i < n; i++){
            int num = Integer.parseInt(st.nextToken());
            if(num == v){
                cnt++;
            }
        }
        System.out.println(cnt);

    }
}