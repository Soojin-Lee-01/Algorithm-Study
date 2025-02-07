import java.util.*;

public class Main{
    public int solution(int k, int[]data) {
       int answer = -1;
       TreeSet<Integer> Tset = new TreeSet<>(Collections.reverseOrder());

       for (int i = 0 ; i < data.length ; i++) {
           for (int j = i + 1 ; j < data.length ; j++) {
               for (int m = j+1 ; m < data.length ;m++) {
                   Tset.add(data[i] + data[j] + data[m]);
               }
           }
       }
       int cnt = 0;
       for (int x : Tset) {
           cnt++;
           if (cnt == k) return x;
       }
       return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T= new Main();
        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int[] data = new int[n];
        for (int i = 0 ; i < n ; i++) {
            data[i] = scanner.nextInt();
        }
        System.out.println(T.solution(k, data));
    }
}
