import java.io.*;
import java.util.*;
import java.nio.file.*;

public class EditDistanceTwoString {

    private static int min(int a, int b, int c) {
        int value = -1;

        if (a >= b && a >= c)
            value =  b >= c ? c : b;
        else if (b >= a && b >= c)
            value =  a >= c ? c : a;
        else if (c >= a && c >= b)
            value =  a >= b ? b : a;

        return value;
    }

    private static int dpEditDistanceTwoString(String s1, String s2, int M, int N) {
        int[][] result = new int[M + 1][N + 1];

        for (int i = 0 ; i < M + 1 ; i++) {
            for (int j = 0 ; j < N + 1 ; j++) {
                if (i == 0 || j == 0) {
                    result[i][j] = i + j;
                } else {
                    int insertion = result[i][j - 1] + 1;
                    int deletion = result[i - 1][j] + 1;
                    int mismatchOrMatch = result[i - 1][j - 1] + (s1.charAt(i - 1) == s2.charAt(j - 1) ? 0 : 1);

                    result[i][j] = min(insertion, deletion, mismatchOrMatch);
                }
            }
        }

        /*for (int[] arr : result) {
            for (int i : arr) {
                System.out.print(i + " ");
            }
            System.out.println();
        }*/

        return result[M][N];
    }

    public static void main(String[] args) {
        /*FastScanner scanner = new FastScanner(System.in);
        String s1 = scanner.next();
        String s2 = scanner.next();

        System.out.println(dpEditDistanceTwoString(s1, s2, s1.length(), s2.length()));*/

        try {
            FastScanner scanner = new FastScanner(Files.newInputStream(Paths.get("./sample/5_3_edit_distance.in")));
            String s1 = scanner.next();
            String s2 = scanner.next();

            System.out.println(dpEditDistanceTwoString(s1, s2, s1.length(), s2.length()));
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }

    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner (InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
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
