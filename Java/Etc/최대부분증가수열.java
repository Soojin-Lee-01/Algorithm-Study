import java.util.*;

public class Main{
   static int[] dy;
   public int solution(int n, int[]data) {
       int answer = 0;
       dy = new int[n];
       dy[0] = 1;
       for(int i = 1 ; i < data.length ;i++) {
          int max = 0;
          for (int j = i-1; j >= 0 ;j--) {
              if (data[j] < data[i] && dy[j] > max) {
                  max = dy[j];
              }
          }
          dy[i] = max + 1;
          answer = Math.max(dy[i], answer);
       }
       return answer;
   }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T= new Main();
        int n = scanner.nextInt();
        int[] data = new int[n];

        for (int i = 0 ; i < n ; i++) {
            data[i] = scanner.nextInt();
        }
        System.out.println(T.solution(n, data));
    }
}
