class Solution {
    public int temp(int num) {
        if (num % 2 == 0 || num == 0) {
            return 1;
        } else {
            return 0;
        }
    }
    public String solution(int num) {
        String answer = "";
        if (temp(num) == 1) {
            answer = "Even";
        } else {
            answer = "Odd";
        }
        return answer;
    }
}
