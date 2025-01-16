/*
문제 : 교육과정 설계

수업계획을 짜야하는 상황.
필수과목 반드시 이수, 순서도 똑같아야함!
ABC 순서대로 이수, 순서도 똑같아야함
ex) ASDBC -> 0 / ADSCB -> X

[IDEA]
- Queue를 이용하면 되지 않을까!
- 수업이 한번 나온다는 제한이 없으므로 중복할 수도 있음

1) 정상 계획을 queue에 넣어주고 비교한다.
2) 계획한 과목의 길이만큼 순회하면서, 만약 앞의 과목이 contain이고 정상계획은 맨 앞과 같아면 poll()
3) 그게 아니라면 바로 return "NO"
4) 마지막으로 최종으로 정상 계획의 queue가 비어있지 않다면 return "N0" 그게 아니라면 return "YES"

[Point!!!!!!!]
- 만약 person_plan 길이만큼 순회한다면 틀린다!!!
왜냐하면, 큐에서 제거하는 과정에서 person_plan의 길이도 자동으로 줄어들고 있기 때문!!
따라서, person_plan이 empty될 때까지 반복한다.
*/

import java.util.*;

public class Main {
    public String solution(String correct_plan, String plan) {
        String answer = "YES";
        Queue<Character> good_plan = new LinkedList<>();

        for (char n : correct_plan.toCharArray()) good_plan.offer(n);
        for (char x : plan.toCharArray()) {
            if (good_plan.contains(x)) {
                if (x != good_plan.poll()) return "NO";
            }
        }
        if (!good_plan.isEmpty()) answer = "NO";
        return answer;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Main T = new Main();
        String correct_plan = scanner.next();
        String plan = scanner.next();

        System.out.println(T.solution(correct_plan, plan));
    }
}
