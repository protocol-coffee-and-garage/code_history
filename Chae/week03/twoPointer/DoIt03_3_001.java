import java.util.Scanner;

public class DoIt03_3_001 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  //연속된 수를 합해서 만들 수
        int count = 1; //n하나만 골랐을 때로 초기화
        int startIndex = 1;
        int endIndex = 1;
        int sum = 1;  //포인터들이 1부터 시작하기 때문에 1로 초기화

        while(endIndex != n){
            if(sum == n ){
                count++;
                endIndex++;
                sum = sum + endIndex;
            }else if(sum > n){
                sum = sum - startIndex; //기존 더해진 수 빼고
                startIndex++; //오른쪽으로
            }else{ //sum < n
                endIndex++;
                sum = sum + endIndex;

            }
        }
        System.out.println(count);
    }
}
