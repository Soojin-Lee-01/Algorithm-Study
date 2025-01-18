/*
문제 : 버블 정렬

버블 정렬로 배열을 정렬하기

시간복잡도 : O(n**2)
*/

import java.util.*;

public class Main {
    public int[] solution(int n, int[] nums) {

        // 버블 정렬
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    int temp = nums[j + 1];
                    nums[j + 1] = nums[j];
                    nums[j] = temp;
                }
            }
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
