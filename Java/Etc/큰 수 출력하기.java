import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public ArrayList<Integer> solution (int[] data) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(data[0]);

        for (int i = 0 ; i < data.length-1 ; i++) {
            if (data[i] < data[i+1]) {
                answer.add(data[i+1]);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int[] arr = new int[num];
        for (int i = 0 ; i < num ; i++) {
            int n = scanner.nextInt();
            arr[i] = n;
        }
        for (int x : T.solution(arr)) {
            System.out.print(x + " ");
        }
    }
}
