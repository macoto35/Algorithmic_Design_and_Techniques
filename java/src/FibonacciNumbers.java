import java.io.*;
import java.util.*;

public class FibonacciNumbers {
	
	public static long naiveSol(int n) {
		if (n <= 1) {
			return n;
		}
		
		return naiveSol(n - 1) + naiveSol(n - 2);
	}
	
	public static long fastSol(int n) {
		long[] arr = new long[n + 1];
		arr[0] = 0;

		if (n > 0) {
			arr[1] = 1;
		}

		for(int i = 2 ; i < n + 1 ; i++) {
			arr[i] = arr[i - 1] + arr[i - 2];
		}
		
		return arr[n];
	}

	public static void main(String[] args) {
		/*FastScanner scanner = new FastScanner(System.in);
		int n = scanner.nextInt();
		System.out.println(naiveSol(n));
		System.out.println(fastSol(n));*/
		
		boolean result = true;
		int n = 0;
		while (result && n <= 45) {
			if (naiveSol(n) == fastSol(n)) {
				System.out.println(n + " -  ok" );
				n++;
			} else {
				System.out.println(n + " -  fail" );
				result = false;
			}
		}
	}
	
	static class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		public FastScanner(InputStream is) {
			try {
				br = new BufferedReader(new InputStreamReader(is));
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
		
		public String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}
		
		public int nextInt() {
			return Integer.parseInt(next());
		}
	}
}
