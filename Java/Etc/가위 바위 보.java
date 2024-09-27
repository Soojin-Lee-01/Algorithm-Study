import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public ArrayList<Character> solution (int[] data1, int[] data2) {
        ArrayList<Character> answer = new ArrayList<>();

        for (int i = 0 ; i < data1.length ;i++) {
            if (data1[i] == data2[i]) {
                answer.add('D');
            }
            else if (data1[i] == 2 && data2[i] == 1) {
                answer.add('A');
            }
            else if (data1[i] == 1 && data2[i] == 3) {
                answer.add('A');
            }
            else if (data1[i] == 3 && data2[i] == 2) {
                answer.add('A');
            } else {
                answer.add('B');
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int[] data1 = new int[num];
        int[] data2 = new int[num];
        for (int i = 0; i < num ; i++) {
            int n = scanner.nextInt();
            data1[i] = n;
        }
        for (int i = 0; i < num ; i++) {
            int n = scanner.nextInt();
            data2[i] = n;
        }

        for (char x : T.solution(data1, data2)) {
            System.out.println(x);
        }

    }
}

