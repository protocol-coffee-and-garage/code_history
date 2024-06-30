import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.ExecutionException;

public class BackJ_11478 {
    public static void main(String[] args) throws Exception {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String str = bf.readLine();
        Set<String> set = new HashSet<>();

        for(int i = 0; i <= str.length(); i++){
            for(int j = 0; j < i; j++){
                set.add(str.substring(j, i));
            }
        }
        System.out.println(set.size());
    }
}
