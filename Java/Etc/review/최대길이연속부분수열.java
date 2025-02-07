import java.util.*;

import static java.lang.Math.abs;
import static java.lang.Math.min;

public class Main{
    public int solution(int m, int[] data) {
       int answer = 0;
       int left = 0;
       int temp = 0;

       for (int i = 0 ; i < data.length; i++) {
           if (data[i] == 0) temp++;

           while (temp > m) {
               if (data[left] == 0) temp--;
               left++;
           }
           answer = Math.max(answer, i-left+1);
       }
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.nextLine();

        Main T = new Main();

        int[] data = new int[n];

        for (int i = 0 ; i < n ; i++) {
            data[i] = scanner.nextInt();
        }
        scanner.close();

        System.out.println(T.solution(m, data));
    }
}
