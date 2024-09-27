import java.util.Scanner;

public class Main {

    public String solution(String word) {
        String answer = "";
        int count = 1;

        word += ' ';

        for (int i = 0 ; i < word.length()-1 ; i++) {
            if (word.charAt(i) == word.charAt(i+1)) count++;
            else {
                answer += word.charAt(i);
                if (count > 1) answer += String.valueOf(count);
                count = 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();

        System.out.println(T.solution(word));
    }

}
