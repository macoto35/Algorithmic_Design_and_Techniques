package algo;

import java.io.*;
import java.util.StringTokenizer;

import java.util.*;

public class CollectionSignature {

	private static List<Integer> greedyFast(List<Pair> arr) {
		int maxRightPoint = 0;
		List<Integer> res = new ArrayList<Integer>();
		
		while (arr.size() > 0) {
			res.add(arr.get(0).y);
			maxRightPoint = arr.get(0).y;
			
			Iterator<Pair> it = arr.iterator();
			while (it.hasNext()) {
				Pair tmp = it.next();
				if (tmp.x <= maxRightPoint && tmp.y >= maxRightPoint)
					it.remove();
			}
		}
		
		return res;
	}
	
	public static void main(String[] args) {
		FastScanner scanner = new FastScanner(System.in);
		
		int n = scanner.nextInt();
		
		List<Pair> arr = new ArrayList<Pair>();
		for (int i = 0 ; i < n ; i++) {
			arr.add(new Pair(scanner.nextInt(), scanner.nextInt()));
		}
		
		arr.sort(Comparator.comparing((Pair p) -> p.y));
		
		System.out.println(greedyFast(arr).size());
	}
	
	public static class Pair {
		int x;
		int y;
		
		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}
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
			while (st == null || !st.hasMoreTokens()) {
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
	}
	
}
