import java.util.*;

public class Main {
    // 아예 괄호가 있으면 넣어주지 않고 answer에 추가해주는 방식
    public String solution(String data) {
        String answer = "";
        Stack<Character> stack = new Stack<>();

        for (char x : data.toCharArray()) {
            if (x == '(') stack.push(x);
            else {
                if (stack.isEmpty()) answer += x;
                else if (x == ')') {
                    stack.pop();
                }
            }
        }
        return answer;
    }
    // 다 넣어주고 괄호를 제거하고 남을 것을 answer에 추가해주는 방식
    public String solution2(String data) {
        String answer = "";
        Stack<Character> stack = new Stack<>();

        for (char x : data.toCharArray()) {
            if (x == ')') {
                while (stack.pop() != '(');
            } else stack.push(x);
        }
        for (int i = 0 ; i < stack.size() ; i ++) answer += stack.get(i);

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String data = scanner.next();

        System.out.println(T.solution2(data));
    }
}
