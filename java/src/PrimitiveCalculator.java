import java.util.*;

public class PrimitiveCalculator {

    private static int dpCalculator(int num, int[] primitives) {
        int[] result = new int[num + 1];
        for (int i = 0 ; i < num + 1 ; i++)
            if(i < 2)
                result[i] = 0;
            else
                result[i] = 99999;

        for (int n = 2 ; n < num + 1; n++) {
            int minCnt = 99999;

            for (int p : primitives) {
                if (n >= p) {
                    if (p == 1)
                        minCnt = result[n - 1] + 1;
                    else if (n % p == 0)
                        minCnt = result[n / p] + 1;

                    if (result[n] > minCnt)
                        result[n] = minCnt;
                }
            }
        }

        return result[num];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();

        System.out.println(dpCalculator(n, new int[]{1, 2, 3}));
    }
}
