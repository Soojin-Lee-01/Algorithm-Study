import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Brick{
    int width, height, weight;

    public Brick(int width, int height, int weight) {
        this.width = width;
        this.height = height;
        this.weight = weight;
    }
}

class TowerBuilder {
    private List<Brick> bricks;
    private int[] dp;

    public TowerBuilder(List<Brick> bricks) {
        this.bricks = bricks;
        this.dp = new int[bricks.size()];
    }

    public int buildTallest() {
        bricks.sort((b1, b2) -> Integer.compare(b2.width, b1.width));

        int maxHeight = 0;

        for (int i = 0; i < bricks.size() ;i++) {
            dp[i] = bricks.get(i).height;

            for (int j = 0 ; j < i ;j++) {
                if (bricks.get(i).weight < bricks.get(j).weight) {
                    dp[i] = Math.max(dp[i], dp[j] + bricks.get(i).height);
                }
            }
            maxHeight = Math.max(maxHeight, dp[i]);
        }

        return maxHeight;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        List<Brick> bricks = new ArrayList<>();

        for (int i = 0 ; i < N ; i++) {
            int width = scanner.nextInt();
            int height = scanner.nextInt();
            int weight = scanner.nextInt();
            bricks.add(new Brick(width, height, weight));
        }
        scanner.close();

        TowerBuilder towerBuilder = new TowerBuilder(bricks);
        int result = towerBuilder.buildTallest();

        System.out.println(result);
    }
}
