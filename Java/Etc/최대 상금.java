import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;
 
public class Solution {
    public static int answer;
    public static Set<String> visited;
 
    public static void dfs(char[] data, int n, int count) {
        if(n == count) {
            answer = Math.max(answer, Integer.parseInt(String.valueOf(data)));
            return;
        }
 
        for (int i = 0 ; i <data.length-1 ; i++) {
            for (int j = i+1 ; j < data.length ;j++) {
                char temp = data[i];
                data[i] = data[j];
                data[j] = temp;
                String key = n + String.valueOf(data);
                if (!visited.contains(key)) {
                    visited.add(key);
                    dfs(data, n+1, count);
                }
                temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int test = scanner.nextInt();
        for (int i = 0 ; i < test ; i++) {
            answer = 0;
            String data = scanner.next();
            int count = scanner.nextInt();
            visited = new HashSet<>();
            dfs(data.toCharArray(), 0, count);
            System.out.println("#" + (i+1) + " " + answer);
 
        }
    }
}
