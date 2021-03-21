package testCode.testPack.test1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/*
 * 주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌

김씨와 이씨는 각각 몇 명 인가요?
"이재영"이란 이름이 몇 번 반복되나요?
중복을 제거한 이름을 출력하세요.
중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
 */

public class synapsoft_employment_test {

	String names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌";
	String[] name = names.split(",");
	String nameResult = "";
	ArrayList<String> AS = new ArrayList<>();

	public void test() {

		int countNameK = 0;
		int countNameE = 0;
		int countNameEJY = 0;

		Arrays.sort(name);

		for (int i = 0; i < name.length; i++) {

			if (name[i].charAt(0) == '김') {
				nameInput(i);
				nameInputArray(i);
				countNameK++;

			} else if (name[i].contains("이재영")) {
				nameInput(i);
				nameInputArray(i);
				countNameEJY++;
			} else if (name[i].charAt(0) == '이') {
				countNameE++;
				nameInput(i);
				nameInputArray(i);

			} else {
				nameInput(i);
				nameInputArray(i);
			}

		}
		Collections.sort(AS);
		System.out.println("arrayList " + AS); // 배열과 ArrayList에 따라 작동 구조에 따라 sort 순서도 달라진다.
		System.out.println("array" + nameResult);
		System.out.println(
				"count " + "이씨성 숫자" + (countNameE + countNameEJY) + " 이재영 숫자" + countNameEJY + " 김씨성 숫자" + countNameK);

	}

	public void nameInput(int i) {
		if (!nameResult.contains(name[i])) {
			nameResult += ", " + String.valueOf(name[i]);
		}
	}

	public void nameInputArray(int i) {
		if (!AS.contains(name[i])) {
			AS.add(name[i]);
		}
	}
	
	/* 
	 * ***다른 사람의 풀이 방법 
	 * 
	 *  String input = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌";
        String[] names = input.split(",");

        int count_kim = 0;
        int count_lee = 0;
        int count_ljy = 0;
        ArrayList<String> name_list = new ArrayList<String>();

        for(int i = 0; i < names.length; i++) {
            if(names[i].startsWith("김"))
                count_kim++;
            if(names[i].startsWith("이"))
                count_lee++;
            if(names[i].equals("이재영"))
                count_ljy++;
            if(!name_list.contains(names[i]))
                name_list.add(names[i]);
        }
        String[] name_arr = name_list.toArray(new String[name_list.size()]);

        System.out.println("김 씨: " + count_kim);
        System.out.println("이 씨: " + count_lee);

        System.out.println("이재영 씨: " + count_ljy);

        System.out.println("중복을 제거한 이름: ");
        for(int i = 0; i < name_arr.length; i++)
            System.out.print(name_arr[i] + ((name_arr.length == i + 1)?"\n":", "));

        Arrays.sort(name_arr);
        System.out.println("중복을 제거한 이름을 오름차순으로: ");
        for(int i = 0; i < name_arr.length; i++)
            System.out.print(name_arr[i] + ((name_arr.length == i + 1)?"\n":", "));

    }
	 * 
	 */

}
