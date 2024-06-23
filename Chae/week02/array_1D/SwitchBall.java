import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class SwitchBall {
    public static void main(String[] args) throws Exception{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken()); // 바구니 개수
        int m = Integer.parseInt(st.nextToken()); // 교환 횟수

        ArrayList<Integer> arr = new ArrayList<>();

        for(int b = 0 ; b < n; b++ ) { //바구니 초기 세팅
            arr.add(b + 1);
        }

        for(int s = 0 ; s < m; s++ ) { //교환

            st = new StringTokenizer(bf.readLine());

            if(st.hasMoreTokens()) {
                  int i = Integer.parseInt(st.nextToken()) -1 ; //교환 바구니1 인덱스
                  int j = Integer.parseInt(st.nextToken()) -1 ; //교환 바구니2 인덱스

                  int temp = arr.get(i); //인덱스 0 값

                  arr.add(i, arr.get(j));
                  arr.remove(j+1);
                  arr.add(j+1, temp);
                  arr.remove(i+1);

            }
        }
        for (Integer r : arr) {
            System.out.print(r + " ");
        }
    }
}
