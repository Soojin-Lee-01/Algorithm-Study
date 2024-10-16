import java.util.*;

public class Main {
    public String number(int n ,  int k) {
        String temp = "";

        while (n > 0) {
            temp = String.valueOf(n % k) + temp;
            n = n / k;
        }

        return temp.isEmpty() ? "0" : temp;
    }
    public boolean isPrime(int da) {
        if (da <= 1) return false;

        for (int j = 2 ; j < (int) Math.sqrt(da)+1 ; j++) {
            if (da % j == 0) return false;
        }
        return true;
    }
    public int solution (int n, int k) {
      int answer = 0;

      String te = number(n, k);

      String[] data = te.split("0");

      for (int i = 0 ; i < data.length ; i++) {
          if (!data[i].equals("")) {
              if (isPrime(Integer.parseInt(data[i]))) answer++;
          }
      }

      return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int k = scanner.nextInt();

        System.out.print(T.solution(n, k));
    }
}
