import java.util.*;
import java.io.*;

public class CelebrationParty {

	
	public static void greedy(int[] ages) {
		String segment = "";
		int left = 0, l = 0, r = 0;
		
		while (left < ages.length) {
			l = ages[left];
			r = l + 2;
			
			while (left < ages.length && ages[left] <= r) {
				segment += ages[left] + ",";
				left += 1;
			}
			System.out.println(segment);
			segment = "";
		}
	}
	
	public static void main(String[] args) {
		FastScanner scanner = new FastScanner(System.in);
		
		int n = scanner.nextInt();
		
		int[] ages = new int[n];
		for (int i = 0 ; i < n ; i++)
			ages[i] = scanner.nextInt();
		
		greedy(ages);
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
