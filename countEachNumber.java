package testCode.testPack.test1;

public class countEachNumber {
//1~1000에서 각 숫자의 개수 구하기
//	예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자
//
//	10 = 1, 0
//	11 = 1, 1
//	12 = 1, 2
//	13 = 1, 3
//	14 = 1, 4
//	15 = 1, 5

	public void test1(int[] n) {

		for (int i = 1; i < n.length; i++) {
			System.out.println(i + " " + n[i]);
		}

	}

	public int[] test2() {
		int n = 222;

		int[] box = new int[10];

		for (int i = 1; i < n; i++) {
			box[i % 10]++;
			if (i >= 10) {
				box[i / 10 % 10]++;
			} else if (i >= 100) {
				box[i / 100 % 10]++;
			} else if (i == 1000) {
				box[i / 1000 % 10]++;
			}

		}
		return box;
	}

	public int[] test3() {
		int[] box = new int[10];
		for (int i = 10; i < 16; i++) {
			box[i % 10]++;
			if (i >= 10) {
				box[i / 10 % 10]++;
			} else if (i >= 100) {
				box[i / 100 % 10]++;
			} else if (i == 1000) {
				box[i / 1000 % 10]++;
			}
		}
		return box;
	}
}
