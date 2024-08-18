/*BackJoon 2750*/
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class DoIt_04_1_015 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //정렬할 수 개수
        int[] arr = new int[n];
        for(int i = 0; i < n; i ++){
            int k = Integer.parseInt(br.readLine());
           arr[i] = k;
        }
        for(int i = 0; i < n-1; i++){ //마지막 인덱스 하나 전까지
            for(int j = 0; j < n-1-i; j++){ //오른쪽부터 정렬되기 때문에 n-1-i
                if(arr[j] > arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;

               }
            }
        }
        for(int r : arr){
            System.out.println(r);
        }
    }
}
