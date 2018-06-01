import java.nio.file.*;
import java.util.*;
import java.io.*;

public class MaxAmountGold {
    private static int dpMaxAmountGold(int W, int n, int[] golds) {
        int[][] result = new int[W + 1][n + 1];

        int value = 0;
        for (int i = 0 ; i < n + 1 ; i++) {
            value = 0;
            for (int w = 0 ; w < W + 1 ; w++) {
                if (i == 0 || w == 0) {
                    result[w][i] = 0;
                } else {
                    result[w][i] = result[w][i - 1];
                    if (golds[i - 1] <= w) {
                        value = result[w - golds[i - 1]][i - 1] + golds[i - 1];
                        if (value > result[w][i])
                            result[w][i] = value;
                    }
                }
            }
        }



        return result[W][n];
    }

    public static void main(String[] args) {
        try {
            // Scanner scanner = new Scanner(System.in);
            Scanner scanner = new Scanner(Files.newInputStream(Paths.get("./sample/6_1_knapsack.in")));
            int W = scanner.nextInt();
            int n = scanner.nextInt();

            int[] golds = new int[n];
            for (int i = 0; i < n; i++)
                golds[i] = scanner.nextInt();

            System.out.println(dpMaxAmountGold(W, n, golds));
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
