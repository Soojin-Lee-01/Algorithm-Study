import java.util.Scanner;
 
class Solution {
 
    public int solution(int n, int[] data) {
        int answer = 0;
 
        for (int i = 2; i < n - 2; i++) {
            int leftMax = Math.max(data[i - 2], data[i - 1]);
            int rightMax = Math.max(data[i + 1], data[i + 2]);

            if (data[i] > leftMax && data[i] > rightMax) {
                answer += data[i] - Math.max(leftMax, rightMax);
            }
        }
        return answer;
    }
 
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner scanner = new Scanner(System.in);
 
        for (int testCase = 1; testCase <= 10; testCase++) {
            int n = scanner.nextInt();
            int[] data = new int[n];
            for (int j = 0; j < n; j++) {
                data[j] = scanner.nextInt();
            }
            System.out.println("#" + testCase + " " + solution.solution(n, data));
        }
    }
}
