import java.util.*;
import javax.script.*;

public class maxValArithmeticExpression {
    private static ScriptEngine ENGINE = new ScriptEngineManager().getEngineByName("js");

    private static int parentheses(int[] num, char[] oper) {
        int n = num.length;

        int[][] m = new int[n][n];
        int[][] M = new int[n][n];

        for (int i = 0 ; i < n ; i++)
            m[i][i] = M[i][i] = num[i];

        int j = 0;
        for (int s = 1 ; s < n ; s++) {
            for (int i = 0 ; i < n - s ; i++) {
                j = i + s;
                int[] result = minAndMax(m, M, oper, i, j);
                m[i][j] = result[0];
                M[i][j] = result[1];
            }
        }

        return M[0][n - 1];
    }

    private static int min(int... args) {
        List<Integer> list = new ArrayList<Integer>();
        for (int i : args) {
            list.add(i);
        }

        return Collections.min(list);
    }

    private static int max(int... args) {
        List<Integer> list = new ArrayList<Integer>();
        for (int i : args) {
            list.add(i);
        }

        return Collections.max(list);
    }

    private static int[] minAndMax(int[][] m, int[][] M, char[] oper, int i, int j) {
        int minVal = 99999;
        int maxVal = -99999;

        try {
            for (int k = i; k < j; k++) {
                int a = (int) ENGINE.eval("("+ M[i][k] + ")" + oper[k] + "(" + M[k + 1][j] + ")" );
                int b = (int) ENGINE.eval("("+ M[i][k] + ")" + oper[k] + "(" + m[k + 1][j] + ")" );
                int c = (int) ENGINE.eval("("+ m[i][k] + ")" + oper[k] + "(" + M[k + 1][j] + ")" );
                int d = (int) ENGINE.eval("("+ m[i][k] + ")" + oper[k] + "(" + m[k + 1][j] + ")" );

                minVal = min(minVal, a, b, c, d);
                maxVal = max(maxVal, a, b, c, d);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        } finally {
            return new int[]{minVal, maxVal};
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();

        int size = (int) Math.ceil(s.length() / 2);
        int[] num = new int[size + 1];
        char[] oper = new char[size];

        int i = 0, j = 0;
        for (int k = 0 ; k < s.length() ; k++) {
            char c = s.charAt(k);

            if (k % 2 == 0)
                num[i++] = c - '0';
            else
                oper[j++] = c;
        }

        System.out.println(parentheses(num, oper));
    }
}
