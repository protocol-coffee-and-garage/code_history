import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collection;
import java.util.StringTokenizer;

public class DoIt_04_2_017 {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] carr = br.readLine().toCharArray();
        int n = carr.length;
        int[] arr = new int[n];
        for(int i = 0; i < n ; i++){
            char k = carr[i];
            arr[i] = k - '0';
        }


        for(int i = 0; i < n; i++){
            int max= i;

           for(int j = i+1; j < n; j++){
               if(arr[j] > arr[max]){
                   max = j;    //max가 값이 아니라 max값을 가지고 있는 인덱스임
               }
           }
           if(arr[i] < arr[max]){
               int temp = arr[i];
               arr[i] = arr[max];
               arr[max] = temp;
           }

       }

        for(int r : arr) {
            System.out.print(r);
        }

    }
}


//max = Integer.parseInt(String.valueOf(Arrays.stream(arr).max())); 이렇게 max값을 찾을 경우 max의 인덱스를 찾아야 되는 추가 작업 필요
