import java.util.Scanner;

public class Main {
    public int solution (String str) {
        int answer = 0;
        String temp = "";

        for (int i = 0 ; i < str.length() ; i++) {
            if (!Character.isAlphabetic(str.charAt(i))) {
                temp += str.charAt(i);
            }
        }

        answer = Integer.parseInt(temp);

        return answer;
    }

    public int solution2 (String str) {
        String answer = "";

        for (char x : str.toCharArray()) {
            if (Character.isDigit(x)) answer += x;
        }

        return Integer.parseInt(answer);
    }

    public int solution3 (String str) {
        int answer = 0;

        for (char x : str.toCharArray()) {
            if (x >= 48 && x <= 57) answer = answer * 10 + (x-48);
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();

        System.out.println(T.solution(word));
    }
    
}
