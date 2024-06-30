import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class BackJ_1269 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        long n = Long.parseLong(st.nextToken());  //집합 a의 원소의 개수
        long m = Long.parseLong(st.nextToken());//집합 b의 원소의 개수
        Set<Integer> setA = new HashSet<>();
        Set<Integer> setB = new HashSet<>();

        int cnt = 0;

        st = new StringTokenizer(bf.readLine()); //집합 a
        if(st.hasMoreTokens()){
            for(int i = 0; i<n; i++) {
                setA.add(Integer.parseInt(st.nextToken()));
            }
        }
        st = new StringTokenizer(bf.readLine()); //집합 b
        if(st.hasMoreTokens()){
            for(int i = 0; i<m; i++) {
                setB.add(Integer.parseInt(st.nextToken()));
            }
        }
        for(int a : setA){
            if(!setB.contains(a)){
                cnt++;

            }
        }
        for(int b : setB){
            if(!setA.contains(b)){
                cnt++;
            }
        }
        System.out.println(cnt);

    }

}
