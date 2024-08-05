import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class BackJ_10866 {
    public static void main(String[] args) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());

        Deque<Integer> dq = new ArrayDeque<>();

        for( int i = 0 ; i < n ; i++){
           String input = st.nextToken(bf.readLine());
            switch (input){
                case "push_front":

                    break;
                case "push_back": break;
                case "pop_front": break;
                case "pop_back": break;
                case "size": break;
                case "empty": break;
                case "front": break;
                case "back": break;
            }

        }





    }
}
