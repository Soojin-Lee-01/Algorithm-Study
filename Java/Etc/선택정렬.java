/*
문제 : 선택정렬

선택정렬을 이용해서 배열을 정렬하는 문제

시간복잡도 : O(n**2)
*/
import java.util.*;

public class Main {
    public int[] solution(int n, int[] nums) {
        for (int i = 0; i < n - 1; i++) {
            int temp = nums[i];
            int index = i;
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < temp) {
                    temp = nums[j];
                    index = j;
                }
            }
            nums[index] = nums[i];
            nums[i] = temp;
        }
        return nums;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();

        int n = scanner.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }
        for (int k : T.solution(n, nums)) {
            System.out.print(k + " ");

        }
    }
}
