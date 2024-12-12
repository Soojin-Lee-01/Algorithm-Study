import java.util.Scanner;
/*
문제 : 연속된 자연수의 합 (연속된 2개 이상의 자연수)
ex) N = 15 -> (1+2+3+4+5+), (4+5+6), (7+8) : 3개
Two-Pointer 문제

시간복잡도 : O(n)
*/
public class Main {
    public int solution(int sum) {
        int result = 0;
        int left = 1;
        int right = 1;
        int temp_sum = 0;

        while (left < sum / 2 + 1) {
            if (temp_sum < sum) {
                temp_sum += right;
                right++;
            } else if (temp_sum > sum) {
                temp_sum -= left;
                left++;
            } else{
                if (right-left > 1) result++;
                temp_sum -= left;
                left++;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        System.out.println(T.solution(num));
    }
}
