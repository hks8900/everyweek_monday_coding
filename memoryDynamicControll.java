package testCode.testPack.test1;

import java.util.Scanner;

public class memoryDynamicControll {

	public void DC() {
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt();
		int resultSc = 0;
		for (int i = 1; i <= n1; i++) {
			System.out.println("정수를 입력하세요 " + i + "번");
			int scInput = sc.nextInt();
			resultSc += scInput;
		}

		System.out.println("ave " + (resultSc / n1));
		System.out.println("sum " + resultSc);
		resultSc = 0;
		n1 = 0;
		System.out.println(resultSc + " " + n1);
	}

}
