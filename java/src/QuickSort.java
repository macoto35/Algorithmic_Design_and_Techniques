public class QuickSort {

	private static void swap(int[] arr, int i, int j) {
		int tmp = arr[i];
		arr[i] = arr[j];
		arr[j] = tmp;
	}
	
	private static MidPivot partition(int[] arr, int l, int r) {
		int x = arr[l];
		int m1 = l, m2 = l;
		
		for (int i = l + 1 ; i < r ; i++) {
			if (arr[i] < x) {
				m1 += 1;
				m2 += 1;
				swap(arr, m2, m1);
				swap(arr, m1, i);
			} else if (arr[i] == x) {
				m2 += 1;
				swap(arr, m2, i);
			}
		}
		swap(arr, l, m1);
		
		return new MidPivot(m1, m2);
	}
	
	private static void selectRandomPivot(int[] arr, int l, int r) {
		int m = l + (int)Math.floor((r - l) / 2);
		
		int a = arr[l];
		int b = arr[m];
		int c = arr[r];
		int mid = -1;

		if (a >= b && a >= c)
			mid = b >= c ? m : r; 
		
		if (b >= a && b >= c)
			mid = a >= c ? l : r;
		
		if (c >= a && c >= b)
			mid = a >= b ? l : m;
		
		swap(arr, l, mid);
	}
	
	private static void quickSort(int[] arr, int l, int r) {
		while (l < r) {
			selectRandomPivot(arr, l, r - 1);
			
			MidPivot midPivot = partition(arr, l, r);
			
			if ((midPivot.m1 - l) < (r - midPivot.m2)) {
				quickSort(arr, l, midPivot.m1 - 1);
				l = midPivot.m2 + 1;
			} else {
				quickSort(arr, midPivot.m2 + 1, r);
				r = midPivot.m1 - 1;
			}
		}
	}
	
	public static void main(String[] args) {
		int[] arr = {1, 4, 2, 8, 7, 7, 9, 11}; // 1 2 4 7 7 8 9 11
		quickSort(arr, 0, arr.length);
		
		for(int i : arr) {
			System.out.print(i + " ");
		}
	}
	
	public static class MidPivot {
		int m1;
		int m2;
		
		public MidPivot(int m1, int m2) {
			this.m1 = m1;
			this.m2 = m2;
		}
	}
}
