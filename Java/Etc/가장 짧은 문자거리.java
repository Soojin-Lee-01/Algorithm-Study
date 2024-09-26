import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public int[] solution(String str, char n) {
        int[] data = new int[str.length()]; // 다 0으로 초기화됨 ! 그게 기본!
        ArrayList<Integer> temp = new ArrayList<>();

        for (int i = 0 ; i < str.length() ; i++) {
            if (str.charAt(i) == n) {
                temp.add(i);
            }
        }
        int check = 0;
        for (int num : temp) {
            for (int j = 0; j < str.length(); j++) {
                if (num > j) {
                    if (check == 0) {
                        data[j] = num - j;
                    } else {
                        if (data[j] > num - j) {
                            data[j] = num - j;
                        }
                    }
                } else if (num < j) {
                    if (check == 0) {
                        data[j] = j - num;
                    } else {
                        if (data[j] > j - num) {
                            data[j] = j - num;
                        }
                    }
                } else {
                    data[j] = 0;
                }
            }
            check = 1;
        }
        return data;
    }

    public int[] solution2 (String str, char n) {
        int[] data = new int[str.length()];
        int p = 10000;
        for (int i = 0 ;i < str.length() ; i++) {
            if (str.charAt(i) == n) p = 0;
            else {

                p++;
                data[i] = p;
            }
        }
        p = 10000;
        for (int i = str.length()-1 ; i >= 0 ; i--) {
            if (str.charAt(i) == n) p = 0;
            else {
                p++;
                data[i] = Math.min(p, data[i]);
            }
        }
        return data;
    }
    public static void main(String[] args) {
        Main T = new Main();
        Scanner scanner = new Scanner(System.in);
        String word = scanner.next();
        char n = scanner.next().charAt(0);
        for(int x : T.solution2(word, n)) {
            System.out.print(x+ " ");
        }
    }

}
