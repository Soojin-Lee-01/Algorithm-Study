class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        int temp = 0;
        for (int i = 0; i < arr.length; i++) {
            temp += arr[i]; 
        }
        answer = (double) temp / arr.length;
        
        return answer;
    }
}
