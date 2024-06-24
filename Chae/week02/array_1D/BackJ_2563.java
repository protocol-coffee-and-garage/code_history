import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BackJ_2563 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int[][] arr = new int[100][100];

        //100*100 0으로 초기화
        for(int i = 0; i < 100; i++){
            for(int j = 0; j < 100; j++){
                arr[i][j] = 0;
            }
        }
        int n = Integer.parseInt(bf.readLine()); //색종이 개수
        int x = 0;
        int y = 0;
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());

            for (int t = x-1; t < x + 9; t++) {   //색종이 10*10인데 (0,0)시작이라서 +9
                for (int j = y-1; j < y + 9; j++) {
                    if (arr[t][j] == 0) {
                        arr[t][j] = 1;
                    }
                }
            }
        }
        for(int i = 0; i <100; i++){
            for(int j = 0; j < 100; j++){
                if(arr[i][j] ==1){
                    cnt++;
                }
            }
        }
        System.out.println(cnt);

    }
}
