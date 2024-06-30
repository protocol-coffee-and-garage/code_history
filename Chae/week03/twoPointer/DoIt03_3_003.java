import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class DoIt03_3_003 {
    public static void main(String[] args) throws Exception {

            BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
            int n = Integer.parseInt(bf.readLine());
            int result = 0;
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int[] a = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);

        for( int k = 0; k < n; k++){ //k는 판별 대상(하나씩 증가하면서 두 수의 합이 k갸 되는지 테스트)
            long find = a[k]; //두 수의 합이 k가 되는 수 = find
            int i = 0;
            int j = n-1;

            while(i < j) {
                if (a[i] + a[j] == find) {
                    if (i != k && j != k) {
                        result++;
                        break;
                    } else if (i == k) {
                        i++;
                    } else if (j == k) {
                        j--;
                    }
                }else if (a[i] + a[j] < find) {
                    i++;
                }else{
                    j--;
                }
            }
        }
        System.out.println(result);
        bf.close();
    }
}
