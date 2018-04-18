package algo;

import java.io.*;
import java.util.*;

public class MaxRevAd {

	private static long greedy(int n, Long[] a, Long[] b)
	{
		long sum = 0;
		
		for(int i = 0 ; i < n ; i++)
			sum += a[i] * b[i];
		
		return sum;
	}
	
	public static void main(String[] args) {
		/*FastScanner scanner = new FastScanner(System.in);
		
		int n = scanner.nextInt();
		Integer[] a = new Integer[n];
		Integer[] b = new Integer[n];
		
		for(int i = 0 ; i < n ; i++)
			a[i] = scanner.nextInt();
		for(int i = 0 ; i < n ; i++)
			b[i] = scanner.nextInt();
		
		Arrays.sort(a, Collections.reverseOrder());
		Arrays.sort(b, Collections.reverseOrder());
		
		System.out.println(greedy(n, a, b));

		scanner.close();*/
		
		try {
			FastScanner scanner = new FastScanner(new FileInputStream("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/3_3_dot_product20180216.in"));
			
			int n = scanner.nextInt();
			Long[] a = new Long[n];
			Long[] b = new Long[n];
			
			for(int i = 0 ; i < n ; i++)
				a[i] = scanner.nextLong();
			for(int i = 0 ; i < n ; i++)
				b[i] = scanner.nextLong();
			
			Arrays.sort(a, Collections.reverseOrder());
			Arrays.sort(b, Collections.reverseOrder());
			
			System.out.println(greedy(n, a, b));
			
			scanner.close();
		} catch(Exception ex) {
			ex.printStackTrace();
		}
	}
	
	public static class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		
		public FastScanner(InputStream is) {
			try {
				br = new BufferedReader(new InputStreamReader(is));
			} catch (Exception ex) {
				ex.printStackTrace();
			}
		}
		
		public String next() {
			while(st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (Exception ex) {
					ex.printStackTrace();
				}
			}
			return st.nextToken();
		}
		
		public int nextInt() {
			return Integer.parseInt(next());
		}
		
		public long nextLong() {
			return Long.parseLong(next());
		}
		
		public void close() {
			try {
				br.close();
			} catch (Exception ex) {
				ex.printStackTrace();
			}
		}
	}
}
