import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.*;

public class Divide42Mod {
    public static void main(String[] args) throws Exception {

        ArrayList<Integer> arr = new ArrayList<>();
        ArrayList<Integer> arr2 = new ArrayList<>();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in) );

        for (int i =0; i < 10; i++) {
            int n = Integer.parseInt(bf.readLine());
            if ( n > 0) {
                int r = n % 42;
                    arr.add(r);
            }
        }
        List<Integer> disList = arr.stream()
                                   .distinct()
                                    .collect(Collectors.toList());

            System.out.println(disList.size());
    }
}
