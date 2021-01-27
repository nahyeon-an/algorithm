package sds03;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

/*
 * 2504 : ��ȣ�� ��
 * () 2��
 * [] 3��
 * j, k : �ּ���, �ִ��� -> ���������� �غ���
 */
public class PracticeE {
	private static Stack<String> st;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		int len = s.length();
		st = new Stack<>();
		
		if (!isCorrect(s)) {
			System.out.println(0);
			return;
		}
		
		for (int i = 0; i < len; i++) {
			if (s.charAt(i)=='(' || s.charAt(i)=='[') {
				st.push(Character.toString(s.charAt(i)));
			}
			
			if (s.charAt(i)==')') {
				String top = st.pop();
				if (top.equals("(")) {
					// �ùٸ� ��ȣ
					st.push("2");
				}
				else if (top.equals("[")) {
					System.out.println(0);
					return; // �ùٸ��� ���� ���
				}
				else {
					int score = Integer.parseInt(top);
					String temp = st.pop();
					while(!temp.equals("(")) {
						score += Integer.parseInt(temp);
						temp = st.pop();
					}
					st.push(Integer.toString(score * 2));
				}
			}
			
			if (s.charAt(i)==']') {
				String top = st.pop();
				if (top.equals("[")) {
					// �ùٸ� ��ȣ
					st.push("3");
				}
				else if (top.equals("(")) {
					System.out.println(0);
					return; // �ùٸ��� ���� ���
				}
				else {
					int score = Integer.parseInt(top);
					String temp = st.pop();
					while(!temp.equals("[")) {
						score += Integer.parseInt(temp);
						temp = st.pop();
					}
					st.push(Integer.toString(score * 3));
				}
			}
		}
		
		int ans = 0;
		while(!st.empty()) {
			ans += Integer.parseInt(st.pop());
		}
		System.out.println(ans);
	}
	
	public static boolean isCorrect(String str) {
		Stack<String> s = new Stack<>();
		int len = str.length();
		for (int i = 0; i < len; i++) {
			if (str.charAt(i)=='('||str.charAt(i)=='[')
					s.push(Character.toString(str.charAt(i)));
			else if (str.charAt(i)==')') {
				if(s.isEmpty()) {
					return false;
				}
				else {
					if(!s.pop().equals("("))
						return false;
				}
			}
			else {
				if(s.isEmpty()) {
					return false;
				}
				else {
					if(!s.pop().equals("["))
						return false;
				}
			}
		}
		return s.isEmpty();
	}
}
