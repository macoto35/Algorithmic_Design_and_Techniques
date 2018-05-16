
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.io.*;

public class MajorityElemt {

    private static int[] scan(int[] arr, int st, int m, int ed, int[] a, int[] b) {
        if (a[0] != -1)
            for(int i = m + 1 ; i < ed + 1 ; i++)
                if (a[0] == arr[i])
                    a[1] += 1;

        if (b[0] != -1)
            for(int i = st ; i < m + 1 ; i++)
                if (b[0] == arr[i])
                    b[1] += 1;

        int majorityCnt = (int) Math.floor((ed - st + 1) / 2);

        if (a[1] > majorityCnt)
            return a;
        else if (b[1] > majorityCnt)
            return b;
        else
            return new int[]{-1, 0};
    }

    private static int[] merge(int[] arr, int st, int m, int ed, int[] a, int[] b) {
        if(a[0] == b[0]) {
            a[1] += b[1];
            return a;
        }

        return scan(arr, st, m, ed, a, b);
    }

    private static int[] findMajorityElemt(int[] arr, int st, int ed) {
        if (st == ed)
            return new int[] { arr[st], 1 } ;

        int m = (int) Math.floor(st + (ed - st) / 2);

        int[] a = findMajorityElemt(arr, st, m);
        int[] b = findMajorityElemt(arr, m + 1, ed);
        return merge(arr, st, m, ed, a, b);
    }

    public static void main(String[] args) {
        try {
            // Scanner scanner = new Scanner(System.in);
            Scanner scanner = new Scanner(Files.newInputStream(Paths.get(".\\sample\\4_2_majority_element.in")));

            int n = scanner.nextInt();
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
                arr[i] = scanner.nextInt();

            int[] result = findMajorityElemt(arr, 0, n - 1);
            System.out.println(result[0] + "/" + result[1]);

            scanner.close();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
    }
}
