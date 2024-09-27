import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public String solution(int n, String word) {
        String answer = "";

        for (int i = 0 ; i < n ; i++) {
            String temp = word.substring(0, 7).replace('#', '1').replace('*', '0');
            int num = Integer.parseInt(temp, 2);
            answer += (char) num;
            word = word.substring(7);
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String word = scanner.next();

        System.out.println(T.solution(n, word));
    }

}

