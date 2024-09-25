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

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();

        System.out.println(T.solution(word));
    }
    
}
