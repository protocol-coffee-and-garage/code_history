import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class DoIt_04_4_019 {
    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine());
        int n = Integer.parseInt(st.nextToken()); //숫자 개수
        int k = Integer.parseInt(st.nextToken()); //찾을 수

        //int s = start index
        //int e = end index

        st = new StringTokenizer(in.readLine());
        int[] arr = new int[n];
        for(int i = 0; i < n ; i++){
            arr[i] = Integer.parseInt(st.nextToken()); //입력 받은 수 배열에 저장
        }
        quickSort(arr, 0, n-1, k-1);
        System.out.println(arr[k-1]);
    }

    public static void quickSort(int[] arr, int s, int e, int k){
        if(s < e){
            int pivot = partition(arr, s, e);
        }
    }

    public static int partition(int[] arr, int s, int e) {
        if (s + 1 == e) {
            if (arr[s] > arr[e]) swap(arr, s, e);
            return e;
        }
        int m = (s + e) / 2; //중앙값
        swap(arr, s, m); //중앙값을 start index로 보내기
        int pivot = arr[s]; //start index를 피벗으로
        int i = s + 1, j = e;
        while (i <= j) {
            while (j >= s + 1 && pivot < arr[j]) { //j >= s+1가 왜 필요한가....?
                j--;                           //피벗값이 j의 값보다 작을 때 j를 왼쪽으로
            }
            while (i <= e && pivot > arr[i]) {  //여기부터
                i++;
            }
            if (i <= j) {
                swap(arr, i++, j++);
            }
        }

        arr[s] = arr[j];
        arr[j] = pivot;
        return j;                               //여기까지 이해안됨.................
    }

    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[i] = temp;
    }

}
