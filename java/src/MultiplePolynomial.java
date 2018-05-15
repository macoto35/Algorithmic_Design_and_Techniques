
public class MultiplePolynomial {

	private static int[] mult(int[] a, int[] b, int n, int ai, int bi) {
		int[] r = new int[2 * n - 1];
		for(int i =  0 ; i < 2 * n - 1 ; i++)
			r[i] = 0;
		
		if(n == 1) {
			int val1 = a.length > ai ? a[ai] : 0;
			int val2 = b.length > bi ? b[bi] : 0;
			r[0] = val1 * val2;
/*System.out.print("n == 1: ");
for(int re : r) { System.out.print(re + "    "); }
System.out.println();*/

			return r;
		}
		
		int d = Math.floorDiv(n, 2);
		
		int idx = 0;
		for(int tmp : mult(a, b, d, ai, bi))
			r[idx++] = tmp;
/*System.out.print(n + "/" + d + "  SS: ");
for(int re : r) { System.out.print(re + "    "); }
System.out.println();*/
        idx = n;
		for(int tmp : mult(a, b, d, ai + d, bi + d))
			r[idx++] = tmp;
/*System.out.print(n + "/" + d + "  BB: ");
for(int re : r) { System.out.print(re + "    "); }
System.out.println();*/
        int[] d0e1 = mult(a, b, d, ai, bi + d);
		int[] d1e0 = mult(a, b, d, ai + d, bi);
		
		idx = 0;
		
		for (int i = d ; i < n + d - 1 ; i++) {
			if (d0e1.length <= idx)
				break;

			r[i] += d0e1[idx] + d1e0[idx];
			idx += 1;
		}
/*System.out.print(n + "/" + d + "  end: ");
for(int re : r) { System.out.print(re + "    "); }
System.out.println();*/
		return r;
	}
	
	public static void main(String[] args) {
		int coefficient = 4;
		int[] A = {3, 2, 5};
		int[] B = {5, 1, 2};
		
		for (int r : mult(A, B, coefficient, 0, 0)) {
			System.out.print(r + "    ");
		}
		System.out.println();
	}
}
