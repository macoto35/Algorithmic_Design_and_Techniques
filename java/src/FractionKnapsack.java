import java.io.*;
import java.util.*;

public class FractionKnapsack {

	private static double greedyFast(int W, int[][] items) {
		double maxValue = 0;
		
		for (int i = 0 ; i < items.length ; i++) {
			if (W == 0)
				break;
			
			int a = Math.min(items[i][1], W);
			maxValue += (double) a * (double) items[i][0] / (double)items[i][1];
			W -= a;
		}
		
		return maxValue;
	}
	
	public static void main(String[] args) {
		//FastScanner scanner = new FastScanner(System.in);
		
		FastScanner scanner = null;
		try {
			scanner = new FastScanner(new FileInputStream("C:/Users/sohee-um/program/workspace/etc/resource/py/sample/3_2_loot.in"));
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		int n = scanner.nextInt();
		int W = scanner.nextInt();
		
		int[][] items = new int[n][2];
		for(int i = 0 ; i < n ; i++) {
			items[i][0] = scanner.nextInt();
			items[i][1] = scanner.nextInt();
		}
		Arrays.sort(items, Comparator.comparing((int[] arr) -> (double) arr[0] / (double) arr[1]).reversed());
		
		//for(int[] item : items) {
		//	System.out.println(item[0] + "	 "+ item[1] + "	 "+ ((double)item[0]/(double)item[1]));
		//}
		
		System.out.println(greedyFast(W, items));	
	}
	
	public static class FastScanner {
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
	}
}
