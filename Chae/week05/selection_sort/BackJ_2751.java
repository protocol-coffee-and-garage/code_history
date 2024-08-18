/*시간초과뜸!*/
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BackJ_2751 {
    public static void main(String[] args) throws Exception{

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

      /*  BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //원소 개수
        int[] arr = new int[n];

        for(int i = 0; i < n ; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
           arr[i] = Integer.parseInt(st.nextToken());
        }
      */
        for(int i = 0; i < n ; i++){
            int min = i;

            for(int j = i+1; j < n; j++){
                if(arr[j] < arr[min]){
                    min = j;
                }
            }
            if(arr[i] > arr[min]){
                int temp = arr[i];
                arr[i] = arr[min];
                arr[min] = temp;
            }

        }
        for(int r : arr) {
            System.out.println(r);
        }

    }
}