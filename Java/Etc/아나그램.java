import java.util.*;

import static java.lang.System.in;

public class Main {

    public String solution (String data1, String data2) {
        String answer = "YES";
        HashMap<Character, Integer> map = new HashMap<>();

        for (char x : data1.toCharArray()) {
            map.put(x, map.getOrDefault(x, 0) + 1);
        }
        for (char x : data2.toCharArray()) {
            if (!map.containsKey(x) || map.get(x) == 0) return "NO";
            map.put(x, map.get(x) - 1);
        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);

        String data1 = scanner.next();
        String data2 = scanner.next();

        System.out.println(T.solution(data1, data2));
    }
}

