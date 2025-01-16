/*
1. 쇠막대기

[문제]
if () -> 인접한 쌍은 레이저
else -> 쇠막대기

answer : 절단된 쇠막대기 수는 총 몇개?

[IDEA]
- stack으로 풀이
1) stack에는 '(' 만 담는다.
2) 만약 인접한 ')'이 존재한다면 stack에서 하나 pop 해주고, answer += 스택의 길이
그리고 stack.clear() 해준다.
3) 만약 그전이 ')'이고, 또 다시 ')'이거라면 stack에 하나 pop 해주고, answer += 1 해준다.
*/

import java.util.*;

public class Main {
    public int solution(String data) {
        int answer = 0;
        Stack<Character> stack = new Stack<>();
        int isSwitch = 0;

        for (char n : data.toCharArray()) {
            if (n == '(') {
                stack.push('(');
                isSwitch = 0;
            } else {
                stack.pop();
                if (isSwitch == 0) {
                    answer += stack.size();
                    isSwitch = 1;
                } else answer += 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        String data = scanner.next();

        System.out.println(T.solution(data));
    }
}
