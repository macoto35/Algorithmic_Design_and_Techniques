import java.util.*;

public class RecursiveChange {
    private static int dpChanges(int money, int[] coins) {
        int[] minCoins = new int[money + 1];
        minCoins[0] = 0;
        int numCoin = 0;

        for (int i = 1 ; i < money + 1 ; i++) {
            minCoins[i] = 99999999;
            for (int coin : coins) {
                if (i >= coin) {
                    numCoin = minCoins[i - coin] + 1;
                    if (numCoin < minCoins[i])
                        minCoins[i] = numCoin;
                }
            }
        }

        return minCoins[money];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int money = scanner.nextInt();
        int[] coins = {4,3,1};

        System.out.println(dpChanges(money, coins));
    }
}
