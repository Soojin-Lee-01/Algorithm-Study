import java.util.*;

public class Main{
    public Character solution (int n, int[] data) {
        char answer = 'U';
        Set<Integer> temp = new HashSet<>();
        for (int i = 0 ; i < data.length ; i++) {
            temp.add(data[i]);
        }
        if (data.length != temp.size()) answer = 'D';
        return answer;
    }

    public String solution2(int n, int[] data) {
        String answer = "U";
        Arrays.sort(data);
        for (int i = 0 ; i < n-1 ; i++) {
            if (data[i] == data[i+1]) return "D";
        } 
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int n = scanner.nextInt();
        int[] data = new int[n];
        for (int i = 0 ; i < data.length ; i++) {
            data[i] = scanner.nextInt();
        }
        System.out.println(T.solution(n, data));
    }
}
