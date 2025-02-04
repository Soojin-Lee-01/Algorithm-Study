import java.util.*;

import static java.lang.Math.abs;
import static java.lang.Math.min;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int target = scanner.nextInt();
        int num = scanner.nextInt();
        HashSet<Integer> data = new HashSet<>();
        if (num > 0) {
            for (int i = 0 ; i < num ; i++){
            int k = scanner.nextInt();
            data.add(k);
            }
        }

        int min_num = abs(target - 100);

        for (int i = 0 ; i < 999999; i++) {
            boolean isBroken = false;
            String temp = String.valueOf(i);
            for (char n : temp.toCharArray()) {
                if(data.contains(Integer.parseInt(String.valueOf(n)))) {
                    isBroken = true;
                    break;
                }
            }
            if (!isBroken){
                min_num = min(min_num, abs(target - i) + temp.length());
            }
        }

        System.out.println(min_num);
    }
}
