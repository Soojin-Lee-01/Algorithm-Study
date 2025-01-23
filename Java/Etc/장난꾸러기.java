/*
문제 : 장난꾸러기
문제 내용:
키가 작은 순서대로 번호를 발급한다. 하지만 철수가 앞 번호를 갖고 싶어 어떤 짝꿍과 자리를 바꾼다.
여기서, 철수가 발급받은 숫자와 짝꿍이 발급받은 숫자는 각각 무엇일까?
*/
import java.util.*;
public class Main{
    public int[] solution(int num, int[] data) {
        int[] answer = new int[2];
        int[] temp = new int[num];
        for (int i = 0 ; i < data.length ; i++) temp[i] = data[i];
        Arrays.sort(temp);
        int count = 0;
        for (int i = 0 ; i < num ; i++) {
            if (count == 2) break;
            if (data[i] != temp[i]) {
                answer[count] = i+1;
                count++;
            }
        }
        Arrays.sort(answer);
        return answer;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int num = scanner.nextInt();
        int[] data = new int[num];
        for (int i = 0 ; i < num ; i++) {
            data[i] = scanner.nextInt();
        }
        for (int k : T.solution(num, data)) System.out.print(k+ " ");
    }
}
