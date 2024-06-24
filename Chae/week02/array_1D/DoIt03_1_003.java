//Backjoon 11659
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class DoIt03_1_003 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken()); //개수
        int qn = Integer.parseInt(st.nextToken()); //질문 수

        long[]S = new long[n+1];

        st = new StringTokenizer(bf.readLine()); //배열


        for(int i = 1; i <= n; i++){
            if(st.hasMoreTokens()){
              S[i] = S[i-1] + Integer.parseInt(st.nextToken());
            }
        }
        for(int q = 0; q < qn; q++){
            st = new StringTokenizer(bf.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            System.out.println( S[j]  - S[i-1]);
        }
    }
}
