import java.util.*;

import static java.lang.System.in;

public class Main {

    public char solution(String data) {
        char answer = ' ';

        HashMap<Character, Integer> stu = new HashMap<>();

        // map.containsKey('A'); 'A'라는 키가 있는지 확인한다.
        // map.size(); 키의 갯수를 알려준다
        // map.remove('A'); 'A'라는 특정 키를 삭제한다.

        for (char x : data.toCharArray()) {
            stu.put(x, stu.getOrDefault(x, 0) + 1);
        }

        int max_num = 0;

        for (char x : stu.keySet()) {
            if (stu.get(x) > max_num) {
                max_num = stu.get(x);
                answer = x;
            }
        }

        return answer;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(in);
        int num = scanner.nextInt();
        String data = scanner.next();

        System.out.println(T.solution(data));

    }
}

