/*
문제 : 응급실

- 응급실 환자 진료 순서를 구하는 문제
- 대기 목록에서 맨 앞 환자보다 위험도가 높은 환자가 대기 목록에 존재하면 이 환자는 맨 뒤로 보냄
- M번째 환자가 진료받는 순서 구하는 문제
- 주의! 0번째 환자부터 시작 ~ 즉, 인덱스는 0부터!

answer : M번째 환자가 진료받는 순서
*/

import java.util.*;

class Person{
    int id;
    int priority;
    public Person(int id, int priority) {
        this.id = id;
        this.priority = priority;
    }
}

public class Main {
    public int solution(int n, int m, int[] arr) {
        int answer = 0;
        Queue<Person> queue = new LinkedList<>();
        for (int i = 0 ; i < n ; i++) {
            queue.offer(new Person(i, arr[i]));
        }
        while (!queue.isEmpty()) {
            Person temp = queue.poll();
            for (Person x : queue) {
                if (x.priority > temp.priority) {
                    queue.offer(temp);
                    temp = null;
                    break;
                }
            }
            if (temp != null) {
                answer++;
                if (temp.id == m) return answer;

            }
        }
        return answer;

    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        int N = scanner.nextInt();
        int target = scanner.nextInt();
        int[] dangerous = new int[N];
        for (int i = 0; i < N; i++) {
            dangerous[i] = scanner.nextInt();
        }

        System.out.println(T.solution(N, target, dangerous));
    }
} 
