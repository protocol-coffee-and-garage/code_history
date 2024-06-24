//Backjoon 11720
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DoIt03_1_001 {

    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int leng = Integer.parseInt(bf.readLine());
        String b = bf.readLine();
        int sum = 0;

        for (char c : b.toCharArray()){
           int n = Integer.parseInt(String.valueOf(c));
            sum += n;
        }
        System.out.println(sum);
    }
}
