import java.io.*;
import java.util.*;
import java.nio.file.*;

public class LongestCommonSubsequenceOfTwo {
    private static int max(int... args) {
        List<Integer> list = new ArrayList();
        for (int i : args)
            list.add(i);

        return Collections.max(list);
    }

    private static int dpLCS(int n, int[] A, int m, int[] B) {
        int[][] result = new int[n + 1][m + 1];

        for (int i = 0 ; i < n + 1 ; i++) {
            for (int j = 0 ; j < m + 1; j++) {
                if (i == 0 || j == 0) {
                    result[i][j] = 0;
                } else {
                    int insertion = result[i][j - 1];
                    int deletion = result[i - 1][j];
                    int mismatchOrMatch = result[i - 1][j - 1] + (A[i - 1] == B[j - 1] ? 1 : 0);

                    result[i][j] = max(insertion, deletion, mismatchOrMatch);
                }
            }
        }

        /*for (int i = 0 ; i < n + 1 ; i++) {
            for (int j = 0 ; j < m + 1; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }*/

        return result[n][m];
    }

    public static void main(String[] args) {
        // FastScanner scanner = new FastScanner(System.in);
        try {
            FastScanner scanner = new FastScanner(Files.newInputStream(Paths.get("./sample/5_4_lcs2.in")));

            int n = scanner.nextInt();
            int[] A = new int[n];
            for (int i = 0; i < n; i++)
                A[i] = scanner.nextInt();

            int m = scanner.nextInt();
            int[] B = new int[m];
            for (int i = 0; i < m; i++)
                B[i] = scanner.nextInt();

            System.out.println(dpLCS(n, A, m, B));
        } catch (Exception e) {
            e.printStackTrace();
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
