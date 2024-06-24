import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BackJ_3052 {
    public static void main(String[] args) throws Exception {

        ArrayList<Integer> arr = new ArrayList<>();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        for (int i = 0; i < 10; i++) {
            int n = Integer.parseInt(bf.readLine());
            if (n > 0) {
                int r = n % 42;
                arr.add(r);
            }
        }
    }
}