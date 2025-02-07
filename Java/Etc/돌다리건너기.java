import java.util.*;

public class Main{
   public static int[] dy;
   public int solution(int n) {
       dy = new int[n+3];
       dy[1] = 1;
       dy[2] = 1;
       for (int i = 3 ; i < n+3 ; i++) {
           dy[i] = dy[i-1] + dy[i-2];
       }
       return dy[n+2];
   }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T= new Main();
        int n = scanner.nextInt();

        System.out.println(T.solution(n));
    }
}
