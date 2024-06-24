//Backjoon 11660
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DoIt03_1_004 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken()); //n*n 배열
        int m = Integer.parseInt(st.nextToken()); //질문 수

        int A[][] = new int[n+1][n+1];

        //기본 배열 초기화
        for(int i = 1 ; i <= n; i++){ //i행
            st = new StringTokenizer(bf.readLine()); //주어진 베열
            for(int j = 1; j <= n ;j++){ //j열
                A[i][j] = Integer.parseInt(st.nextToken()); // 1,1에 첫번째 원소, 1,2에 두번째 원소 => 다 돌고 다음 행(i)으로
            }
        }

        //구간 합 배열 만들기

        // 합 배열 => (4,4) 값을 구한다
        // (4,3)의 값 = (1,1)~(4,3)
        // (3,4)의 값 = (1,1)~(3,4)
        // 겹친 부분 = (1,1) ~ (3,3)
        // (4,3)의 값 + (3,4)의 값 - 겹친 부분(3,3)의  + 원래 배열의 (4,4)의 값
        int D[][] = new int[n+1][n+1];
        for (int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j];
            }
        }

        // 질문 답
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(bf.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            //(x1,y1) ~ (x2,y2)의 값 출력
            // (2,2) ~ (4,4)의 값 -> (1,1)~(1,4)빼고 (1,1)~(4,1)빼고 두번 뺀 값 (1,1) 더해주기

            int res = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1];

            System.out.println(res);

        }

    }
}
