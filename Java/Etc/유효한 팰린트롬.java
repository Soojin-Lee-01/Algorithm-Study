import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public String solution(String str) {
        String answer = "YES";
        String temp = "";

        for(int i = 0 ; i < str.length() ; i++) {
            if (Character.isAlphabetic(str.charAt(i))) {
                temp += str.charAt(i);
            }
        }

        temp = temp.toLowerCase();
        int len = temp.length();

        for (int i = 0 ; i < len / 2 ; i++) {
            if (temp.charAt(i) != temp.charAt(len-i-1)) return "NO";
        }

        return answer;
    }

    public String solution2 (String str) {
        String answer = "NO";

        str = str.toUpperCase().replaceAll("[^A-Z]", "");
        String temp = new StringBuilder(str).reverse().toString();
        if (str.equals(temp)) answer = "YES";

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();

        System.out.println(T.solution(word));

    }
}
