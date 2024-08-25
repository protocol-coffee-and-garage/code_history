import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DoIt_04_5_020 {

    public static  int[] arr, temp;  //전역변수로 설정
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); //숫자 개수

        arr = new int[n+1];
        temp = new int[n+1];

        for(int i = 1; i <= n; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }
    }

    private static void mergeSort(int s, int e){
        if(e - s < 1){  // e가 s보다 커야함
            return;
        }
        int m = s + (e - s) / 2;  //중간 인덱스
        mergeSort(s, m);  //왼쪽 부분 병합 정렬
        mergeSort(m+1, e); //오른쪽 부분 병합 정렬
        for(int i = s; i <= e; i++){
            temp[i] = arr[i];
        }
    }
}
