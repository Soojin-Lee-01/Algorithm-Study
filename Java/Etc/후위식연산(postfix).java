import java.util.*;

public class Main{
    public int solution(String data) {
        Stack<Integer> stack = new Stack<>();
        for (char n : data.toCharArray()) {
            if (Character.isDigit(n)) {
                stack.push(Integer.parseInt(String.valueOf(n)));
            } else {
                int rt = stack.pop();
                int lt = stack.pop();
                if (n == '+') {
                    stack.push(lt+rt);
                } else if (n == '-') {
                    stack.push(lt-rt);
                } else if (n == '*') {
                    stack.push(lt*rt);
                } else {
                    stack.push(lt/rt);
                }
            }
        }
        return stack.pop();
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        String data = scanner.next();
        System.out.println(T.solution(data));
    }
}
