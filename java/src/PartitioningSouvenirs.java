import java.nio.file.*;
import java.util.*;
import java.io.*;

public class PartitioningSouvenirs {

    private static int knapSackWithoutRepetitions(int W, ArrayList<Integer> values) {
        // find knapsack max target value
        int[][] result = new int[W + 1][values.size() + 1];

        for (int i = 0 ; i < values.size() + 1 ; i++) {
            int value = 0;
            for (int w = 0 ; w < W + 1 ; w++) {
                if (w == 0 || i == 0) {
                    result[w][i] = 0;
                } else {
                    result[w][i] = result[w][i - 1];
                    if (values.get(i - 1) <= w) {
                        value = result[w - values.get(i - 1)][i - 1] + values.get(i - 1);
                        if (value > result[w][i])
                            result[w][i] = value;
                    }
                }
            }
        }

        int resultValue = result[W][values.size()];

        // find components and remove from values
        ArrayList<Integer> used = new ArrayList<Integer>();
        int i = values.size();
        int w = W;
        while (i != 0 && w != 0) {
            int curVal = result[w][i];
            int withoutLastItem = result[w][i - 1];

            if (curVal != withoutLastItem) {
                w -= values.get(i - 1);
                used.add(--i);
            } else {
                i--;
            }
        }

        if (used.size() > 0)
            for(int idx : used)
                values.remove(idx);


        return resultValue;
    }

    private static int dpPartitioningSouvenirs(int n, ArrayList<Integer> values, int sum) {
        if (sum % 3 != 0)
            return 0;

        int W = sum / 3;

        int W1 = knapSackWithoutRepetitions(W, values);
        int W2 = knapSackWithoutRepetitions(W, values);
        int W3 = values.stream().mapToInt(Integer::intValue).sum();

        if (W == W1 && W == W2 && W == W3)
            return 1;
        else
            return 0;
    }

    public static void main(String[] args) {
        /*Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int sum = 0;
        int temp = 0;
        ArrayList<Integer> values = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            temp = scanner.nextInt();
            values.add(temp);
            sum += temp;
        }

        System.out.println(dpPartitioningSouvenirs(n, values, sum));*/

        try {
            Scanner scanner = new Scanner(Files.newInputStream(Paths.get("./sample/6_2_souvenirs.in")));


            while(scanner.hasNextInt()) {
                int n = scanner.nextInt();
                ArrayList<Integer> values = new ArrayList<Integer>();
                for (int i = 0; i < n; i++) {
                    values.add(scanner.nextInt());
                }
                int sum = values.stream().mapToInt(Integer::intValue).sum();

                System.out.print(dpPartitioningSouvenirs(n, values, sum));
            }
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
