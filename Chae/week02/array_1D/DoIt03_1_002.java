//Backjoon 1546
import java.util.*;

public class DoIt03_1_002 {
    public static void main(String[] args) throws Exception{

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); //개수
        int A[] = new int[n];
        for (int i = 0; i < n; i++){
            A[i] = sc.nextInt();
        }
        long sum = 0;
        long max = 0;

        for (int i = 0; i < n; i++){
            if(A[i]>max) max = A[i] ;
            sum += A[i];

        }
        System.out.print(sum * 100.0 / max / n);

      /*
      아래껀 실패! -> 다시 확인하기
      BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());

        ArrayList<Integer> arr = new ArrayList<>();

        long sum = 0;

        for (int i = 0; i < n; i++) {
            int score = Integer.parseInt(st.nextToken());
            arr.add(score);
        }
        List<Integer> list = arr.stream().sorted().collect(Collectors.toList());
        long max = (long) list.get(list.size()-1);

        for (int i=0; i < n; i++ ){
            if(arr.get(i) > max) {
                max = arr.get(i);
            }
            sum = sum + arr.get(i);
        }
        long avg = (sum * 100 / max / n );

        System.out.println(avg);*/
    }
}
