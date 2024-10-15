import java.util.*;

public class Main {

    public boolean isPrime(int num) {
        if (num == 1) return false;
        else {
            for (int i = 2 ; i < num ; i++) {
                if (num % i == 0) return false;
            }
        }
        return true;
    }
    public ArrayList<Integer> solution(int[] data) {
        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0 ; i < data.length ; i++) {
            int temp = data[i];
            int res = 0;
            while (temp > 0) {
                int t = temp % 10;
                res = res * 10 + t;
                temp = temp / 10;
            }
            if (isPrime(res)) {
                answer.add(res);
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] data = new int[n];
        for (int i = 0 ; i < n ; i++) {
            int num = scanner.nextInt();
            data[i] = num;
        }
        for (int k : T.solution(data)) {
            System.out.print(k + " ");
        }

    }
}
