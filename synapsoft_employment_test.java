package testCode.testPack.test1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/*
 * �־��� ���ڿ�(���� ���� ��ǥ�� ���еǾ� ����)�� ������ �Ʒ� ������ ���� ���α׷��� �ۼ��ϼ���.

������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������

�达�� �̾��� ���� �� �� �ΰ���?
"���翵"�̶� �̸��� �� �� �ݺ��ǳ���?
�ߺ��� ������ �̸��� ����ϼ���.
�ߺ��� ������ �̸��� ������������ �����Ͽ� ����ϼ���.
 */

public class synapsoft_employment_test {

	String names = "������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������";
	String[] name = names.split(",");
	String nameResult = "";
	ArrayList<String> AS = new ArrayList<>();

	public void test() {

		int countNameK = 0;
		int countNameE = 0;
		int countNameEJY = 0;

		Arrays.sort(name);

		for (int i = 0; i < name.length; i++) {

			if (name[i].charAt(0) == '��') {
				nameInput(i);
				nameInputArray(i);
				countNameK++;

			} else if (name[i].contains("���翵")) {
				nameInput(i);
				nameInputArray(i);
				countNameEJY++;
			} else if (name[i].charAt(0) == '��') {
				countNameE++;
				nameInput(i);
				nameInputArray(i);

			} else {
				nameInput(i);
				nameInputArray(i);
			}

		}
		Collections.sort(AS);
		System.out.println("arrayList " + AS); // �迭�� ArrayList�� ���� �۵� ������ ���� sort ������ �޶�����.
		System.out.println("array" + nameResult);
		System.out.println(
				"count " + "�̾��� ����" + (countNameE + countNameEJY) + " ���翵 ����" + countNameEJY + " �达�� ����" + countNameK);

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
	 * ***�ٸ� ����� Ǯ�� ��� 
	 * 
	 *  String input = "������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������";
        String[] names = input.split(",");

        int count_kim = 0;
        int count_lee = 0;
        int count_ljy = 0;
        ArrayList<String> name_list = new ArrayList<String>();

        for(int i = 0; i < names.length; i++) {
            if(names[i].startsWith("��"))
                count_kim++;
            if(names[i].startsWith("��"))
                count_lee++;
            if(names[i].equals("���翵"))
                count_ljy++;
            if(!name_list.contains(names[i]))
                name_list.add(names[i]);
        }
        String[] name_arr = name_list.toArray(new String[name_list.size()]);

        System.out.println("�� ��: " + count_kim);
        System.out.println("�� ��: " + count_lee);

        System.out.println("���翵 ��: " + count_ljy);

        System.out.println("�ߺ��� ������ �̸�: ");
        for(int i = 0; i < name_arr.length; i++)
            System.out.print(name_arr[i] + ((name_arr.length == i + 1)?"\n":", "));

        Arrays.sort(name_arr);
        System.out.println("�ߺ��� ������ �̸��� ������������: ");
        for(int i = 0; i < name_arr.length; i++)
            System.out.print(name_arr[i] + ((name_arr.length == i + 1)?"\n":", "));

    }
	 * 
	 */

}
