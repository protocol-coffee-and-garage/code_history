import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class DoIt03_4_002 {
    public static void main(String[] args) throws Exception{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken()); //숫자 총 개수
        int s = Integer.parseInt(st.nextToken()); //슬라이딩 윈도우 크기(탐색 배열 크기)

        ArrayList<Integer> arr = new ArrayList<>();

        st = new StringTokenizer(bf.readLine());

        for(int i = 0; i < n; i++){
            arr.add(Integer.parseInt(st.nextToken()));
        }

       for(int i = 0; i+s < n; i++){

       }



    }
}
