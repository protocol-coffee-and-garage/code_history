import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class SmallNum {
    public static void main(String[] args) throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in) );
        StringTokenizer st = new StringTokenizer(bf.readLine()); //첫번째 줄
        int n = Integer.parseInt(st.nextToken());  // N개
        int x = Integer.parseInt(st.nextToken());  // 정수 X

       st = new StringTokenizer(bf.readLine());

        for (int i = 0; i < n; i++ ) {
            if (st.hasMoreTokens()) {
                int num = Integer.parseInt(st.nextToken());
                if (num < x) {
                    System.out.print(num + " ");
                }
            }
        }
    }
}
