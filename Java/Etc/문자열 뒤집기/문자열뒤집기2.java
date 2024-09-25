import java.util.*;

public class Main {
    public String solution(String str) {
        String answer = "";
        StringBuffer sb = new StringBuffer(str);

        answer = sb.reverse().toString();

        return answer;
    }
    public String solution2 (String str) {
        String answer = "";
        for (int i = str.length()-1 ; i >= 0 ; i--) {
            answer += str.charAt(i);
        }

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();

        for (int i = 0 ; i < num ; i++) {
            String word = scanner.next();
            System.out.println(T.solution2(word));
        }
    }
}
