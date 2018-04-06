package algo;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class MaxPairwiseProduct {
	
	public static int maxPairwiseProduct(int[] numbers) {
		int product = 0;
		int n = numbers.length;
		
		for (int i = 0 ; i < n ; i++) {
			for (int j = i + 1 ; j < n; j++) {
				product = Math.max(product, numbers[i] * numbers[j]);
			}
		}
		
		return product;
	}
	
	public static long fastMaxPairwiseProduct(long[] numbers) {
		/*int large = 0;
		int secoundLarge = 0;
		
		for (int i = 0 ; i < numbers.length ; i++) {
			if (large < numbers[i]) {
				secoundLarge = large;
				large = numbers[i];
			} else if (secoundLarge < numbers[i]) {
				secoundLarge = numbers[i];
			}
		}
		
		return large * secoundLarge;*/
		
		Arrays.sort(numbers);
		int n = numbers.length;

		return numbers[n - 1] * numbers[n - 2];
	}
	
	public static void main(String[] args) {
		FastScanner scanner = new FastScanner(System.in);
		int n = scanner.nextInt();
		long[] numbers = new long[n];
		for(int i = 0 ; i < n ; i++) {
			numbers[i] = scanner.nextLong();
		}
		
		// System.out.println(maxPairwiseProduct(numbers));
		System.out.println(fastMaxPairwiseProduct(numbers));
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
			while(st == null || !st.hasMoreTokens()) {
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
		
		public long nextLong() {
			return Long.parseLong(next());
		}
	}
}