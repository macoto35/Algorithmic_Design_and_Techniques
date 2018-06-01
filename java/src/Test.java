import java.util.*;

public class Test {

	/*private static long calc_fib(int n) {
		long[] arr = new long[n + 1];
		arr[0] = 0;

		if (n > 0) {
			arr[1] = 1;
		}

		for(int i = 2 ; i < n + 1 ; i++) {
			arr[i] = arr[i - 1] + arr[i - 2];
		}
		
		return arr[n];
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		
		System.out.println(calc_fib(n));
		in.close();
	}*/

	public static void main(String[] args) {
        GenericSub<Integer> gs = new GenericSub<Integer>();
        gs.setParam1(10);
        gs.setParam2(20);
        System.out.println(gs.printParamNum(gs.getParam1(), gs.getParam2()));

        /*GenericSub<String> gs2 = new GenericSub<String>();
        gs2.setParam1("potato");
        gs2.setParam2("sweet potato");
        System.out.println(gs.printParamNum(gs2.getParam1(), gs2.getParam2()));*/

        String a = "aa";
        String b = "aa";
        System.out.println(a == b);
        System.out.println(a.equals(b));

        String c = new String("java");
        String d = new String("java");
        System.out.println(c == d);
        System.out.println(c.equals(d));

        String e = "help";
        String f = new String("help");
        System.out.println(e == f);
        System.out.println(e.equals(f));



	}

	static class GenericSub<T extends Number> {
	    private T num1;
	    private T num2;

	    public T getParam1() { return num1; }
	    public T getParam2() { return num2;}

	    public void setParam1(T num1) { this.num1 = num1; }
        public void setParam2(T num2) { this.num2 = num2; }

        public <T> StringBuffer printParamNum(T param1, T param2) {
	        StringBuffer sb = new StringBuffer();
	        sb.append("first argument: ");
	        sb.append(param1);
	        sb.append(", second argument: ");
	        sb.append(param2);

	        return sb;
        }

        public Double addParam(T param1, T param2) {
	        Double d1 = param1.doubleValue();
	        Double d2 = param2.doubleValue();

	        return d1 + d2;
        }
    }
}
