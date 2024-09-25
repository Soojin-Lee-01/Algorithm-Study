import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public String solution(String str) {
        String answer = "";
        ArrayList<String> s = new ArrayList<>();

        for (char x : str.toCharArray()) {
            String temp = String.valueOf(x);
            if (!s.contains(temp)) {
                s.add(temp);
            }
        }
        // 자바에서 String.join("", s)을 이용해서 문자열러 변환한다.
        answer = String.join("", s);

        return answer;
    }

    public String solution2 (String str) {
        String answer = "";

        for (int i = 0 ; i < str.length() ; i++) {
            if (str.indexOf(str.charAt(i)) == i) {
                answer += str.charAt(i);
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);

        String sentence = scanner.next();

        System.out.println(T.solution2(sentence));

    }
}
