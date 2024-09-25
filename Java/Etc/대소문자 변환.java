import java.util.*;

public class Main {
    public String solution(String str) {
        String answer = "";
        // Solution - 1 문자열을 char 배열로 바꿔주기!
        for (char x : str.toCharArray()) {
            if (Character.isUpperCase(x)) {
                answer += Character.toLowerCase(x);
            } else {
                answer += Character.toUpperCase(x);
            }
        }
        // Solution - 2 아스키코드를 이용한 풀이!
//        for(char x : str.toCharArray()) {
//            if (x >= 97 && x <= 122) answer += (char)(x-32);
//            else answer += (char)(x+32);
//        }
        // Solution - 3
//        for (int i = 0 ; i < str.length() ; i++) {
//            if (Character.isUpperCase(str.charAt(i))) {
//                answer += Character.toLowerCase(str.charAt(i));
//            } else if (Character.isLowerCase(str.charAt(i))) {
//                answer += Character.toUpperCase(str.charAt(i));
//            }
//        }

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();

        Scanner scanner = new Scanner(System.in);

        String sentence = scanner.nextLine();

        System.out.println(T.solution(sentence));

    }
}
