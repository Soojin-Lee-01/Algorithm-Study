import java.util.*;

public class Main {

    public String solution (String data) {
        String answer = "YES";
        Stack<Character> stack = new Stack<>();

        for (char x : data.toCharArray()) {
            if (x == '(') {
                stack.push(x);
            } else {
                if (stack.isEmpty()) return "NO";
                else{
                    if (stack.get(stack.size()-1) == '(') {
                        stack.pop();
                    } else return "NO";
                }
            }
        }
        if (!stack.isEmpty()) return "NO";
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String data = scanner.next();

        System.out.println(T.solution(data));
    }
}

