import java.io.*;
import java.nio.file.Paths;
import java.util.*;
import java.nio.file.*;

public class LongestCommonSubsequenceOfThree {

    private static int max(int... args) {
        List<Integer> list = new ArrayList();
        for (int i : args) {
            list.add(i);
        }

        return Collections.max(list);
    }

    private static int dpLCS(int n, int[] A, int m, int[] B, int l, int[] C) {
        int[][][] result = new int[n + 1][m + 1][l + 1];

        for (int i = 0 ; i < n + 1 ; i++) {
            for (int j = 0 ; j < m + 1 ; j++) {
                for (int k = 0 ; k < l + 1 ; k++) {
                    if (i == 0 || j == 0 || k == 0) {
                        result[i][j][k] = 0;
                    } else {
                        int a = result[i][j][k - 1];
                        int b = result[i][j - 1][k];
                        int c = result[i - 1][j][k];
                        int d = result[i - 1][j - 1][k];
                        int e = result[i][j - 1][k - 1];
                        int f = result[i - 1][j][k - 1];
                        int g = result[i - 1][j - 1][k - 1] + (A[i - 1] == B[j - 1] && B[j - 1] == C[k - 1] ? 1 : 0);

                        result[i][j][k] = max(a, b, c, d, e, f, g);
                    }
                }
            }
        }

        /*for (int i = 0 ; i < n + 1 ; i++) {
            for (int j = 0 ; j < m + 1 ; j++) {
                for (int k = 0 ; k < l + 1 ; k++) {
                    System.out.print(result[i][j][k] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }*/

        return result[n][m][l];
    }

    public static void main(String[] args) {
        try {
            //FastScanner scanner = new FastScanner(System.in);
            FastScanner scanner = new FastScanner(Files.newInputStream(Paths.get("./sample/5_5_lcs3.in")));
            int n = scanner.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++)
                A[i] = scanner.nextInt();

            int m = scanner.nextInt();
            int[] B = new int[m];
            for (int i = 0; i < m; i++)
                B[i] = scanner.nextInt();

            int l = scanner.nextInt();
            int[] C = new int[l];
            for (int i = 0; i < l; i++)
                C[i] = scanner.nextInt();

            System.out.println(dpLCS(n, A, m, B, l, C));
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }

    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }

        public String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException ioe) {
                    ioe.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public void close() {
            try {
                br.close();
            } catch (IOException ioe) {
                ioe.printStackTrace();
            }
        }

    }
}
