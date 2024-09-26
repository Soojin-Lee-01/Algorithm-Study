import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public ArrayList<Character> solution(String data) {
        ArrayList<Character> answer = new ArrayList<>();
        int count = 0;
        String temp = "";

        for (int i = 0 ; i < data.length() ; i ++) {
            if (i == 0) {
                temp = String.valueOf(data.charAt(i));
                count++;
            } else {
                if (temp.equals(String.valueOf(data.charAt(i)))) {
                    count++;
                } else {
                    answer.add(temp.charAt(0));
                    if (count > 1) {
                        answer.add(String.valueOf(count).charAt(0));
                    }
                    temp = String.valueOf(data.charAt(i));
                    count = 1;

                }
            }
        }

        answer.add(temp.charAt(0));
        if (count > 1) {
            answer.add(String.valueOf(count).charAt(0));
        }

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        for (char x : T.solution(word)) {
            System.out.print(x);
        }

    }

}
