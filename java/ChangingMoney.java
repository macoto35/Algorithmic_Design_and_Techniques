package algo;

import java.util.*;

public class ChangingMoney {
	
	private static int naive(int m) {
		int cnt = -1;
		
		for (int i = 0 ; i < m + 1 ; i++) {
			for (int j = 0 ; j < m + 1 ; j++) {
				for (int k = 0 ; k < m + 1 ; k++) {
					// System.out.println("val: " + (i * 1 + j * 5 + k * 10) + "     m: " + m + "      prev_cnt: " + cnt + "     cnt: " + (i+j+k));
					if (i * 1 + j * 5 + k * 10 == m && (cnt > i + j + k || cnt < 0)) {
						cnt = i + j + k;
					}
				}
			}
		}

		// System.out.println("cnt: " + cnt);
		return cnt;
	}

	private static int greedy(int m) {
		int[] arr = {10, 5, 1};
		int remain = m;
		int cnt = 0;
		
		for (int i : arr) {
			cnt += remain / i;
			remain = remain % i;
		}
		
		return cnt;
	}
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int m = scanner.nextInt();
		System.out.println(greedy(m));
		// System.out.println(naive(m));
		
		/*int M = scanner.nextInt();
		Random rand = new Random();

		while (true) {
			int m = rand.nextInt(M + 1);
			if (naive(m) == greedy(m)) {
				System.out.println(m + " - ok");
			} else {
				System.out.println(m + " - fail");
				break;
			}
		}*/

		scanner.close();
	}
}
