package testCode.testPack.test1;

public class testAnswer {

	public void solution() {
		int n = 123;
		int answer = 0;
		int a = 0;

		while (n > 0) {
			answer += n % 10;
			System.out.println("a  " + answer);
			n /= 10;
			System.out.println("n  " + n);
		}
		System.out.println(answer);
	}
	
}
