import java.util.*;

public class Main {
    public ArrayList<String> solution(int num, String[] str) {
        ArrayList<String> answer = new ArrayList<>();

        for (String x : str) {
            String tmp = new StringBuilder(x).reverse().toString();
            answer.add(tmp);
        }

        return answer;
    }

    public ArrayList<String> solution2 (int num, String[] str) {
        ArrayList<String> answer = new ArrayList<>();

        for (String x : str) {
            char[] s = x.toCharArray();
            int lt = 0, rt = x.length()-1;
            while (lt < rt) {
                char tmp = s[lt];
                s[lt] = s[rt];
                s[rt] = tmp;
                lt++;
                lt--;
            }
            String tmp = String.valueOf(s);
            answer.add(tmp);
        }
        return  answer;

    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);

        int num = scanner.nextInt();

        String[] str = new String[num];
        for (int i = 0 ; i < num ; i++) {
            str[i] = scanner.next();
        }
        for (String x : T.solution(num, str)) {
            System.out.println(x);
        }
    }
}
