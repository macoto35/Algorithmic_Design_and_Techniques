import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.io.*;

public class MaxSalary {

	private static boolean comp(String a, String b) {
		return Integer.parseInt(a + b) > Integer.parseInt(b + a);
	}
	
	private static String greedy(List<String> arr) {
		String answer = "";
		
		while(arr.size() > 0) {
			int idx = 0;
			String maxValue = "0";
			for (int i = 0 ; i < arr.size() ; i++) {
				if (comp(arr.get(i), maxValue)) {
					maxValue = arr.get(i);
					idx = i;
				}
			}
			answer += maxValue;
			arr.remove(idx);
		}
		
		return answer;
	}
	
	public static void main(String[] args) {
		try {
			// Scanner scanner = new Scanner(System.in);
			Scanner scanner = new Scanner(Files.newInputStream(Paths.get("./sample/3_6_largest_number.in")));
			
			int n = scanner.nextInt();
			List<String> arr = new ArrayList<String>();
			for (int i = 0 ; i < n ; i++) {
				arr.add(scanner.next());
			}
			
			System.out.println("result: " + greedy(arr));
			
			scanner.close();
		} catch (Exception ex) {
			ex.printStackTrace();
		}
	}
}
