import java.util.*;

public class MergeSort {

	private static List<Integer> mergeSort(List<Integer> arr, int st, int ed) {
		if (st == ed) {
			return Arrays.asList(arr.get(st));
		}
		
		int m = st + (int) Math.floor((ed - st) / 2);
		List<Integer> A = mergeSort(arr, st, m);
		List<Integer> B = mergeSort(arr, m + 1, ed);
		return merge(A, B);
	}
	
	private static List<Integer> merge(List<Integer> A, List<Integer> B) {
		List<Integer> C = new ArrayList<>();
		
		int idxA = 0, idxB = 0;
		
		while (A.size() > idxA && B.size() > idxB) {
			int a = A.get(idxA);
			int b = B.get(idxB);
			if (a <= b) {
				C.add(a);
				idxA++;
			} else {
				C.add(b);
				idxB++;
			}
		}
		
		for (int i = idxA ; i < A.size() ; i++)
			C.add(A.get(i));

		for (int i = idxB ; i < B.size() ; i++)
			C.add(B.get(i));
		
		return C;
	}
	 
	public static void main(String[] args) {
		List<Integer> arr = Arrays.asList(7,2,5,3,7,13,1,6);
		
		for (int i : mergeSort(arr, 0, arr.size() - 1)) {
			System.out.print(i + " ");
		}
	}
}
