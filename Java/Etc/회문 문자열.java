import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public String solution(String str) {

        str = str.toUpperCase();

        int lt = 0, rt = str.length()-1;
        int temp = 0;
        while (lt < rt) {
            if (str.charAt(lt) == str.charAt(rt)) {
                lt++;
                rt--;
            }
            else {
                temp = -1;
                break;
            }
        }
        if (temp == -1) {
            return "NO";
        } else return "YES";

    }

    public String solution2 (String str) {
        String answer = "YES";

        str = str.toUpperCase();

        int len = str.length();

        for (int i = 0 ; i < len/2; i++) {
            if (str.charAt(i) == str.charAt(len-i-1)) return "NO";
        }
        return answer;
    }

    public String solution3 (String str) {
        String answer = "YES";

        String temp = new StringBuilder(str).reverse().toString();

        if (str.equalsIgnoreCase(temp)) answer = "Yes";

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);

        String word = scanner.next();

        System.out.println(T.solution(word));
    }
}
