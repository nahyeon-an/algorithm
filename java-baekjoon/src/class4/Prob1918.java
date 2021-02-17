package class4;

import java.util.*;
import java.io.*;

/*
 * 1918 : 후위 표기식
 */
public class Prob1918 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		
		Stack<Character> stack = new Stack<>();
		char[] ch = br.readLine().toCharArray();
		for (int i = 0; i<ch.length; i++) {
			if (ch[i]=='(') {
				stack.push(ch[i]);
			}
			else if (ch[i]==')') {
				char c;
				while ((c=stack.pop()) != '(') {
					sb.append(c);
				}
			}
			else if (ch[i]=='*' || ch[i]=='/') {
				while(!stack.isEmpty() && (stack.peek()=='*'||stack.peek()=='/')) {
					sb.append(stack.pop());
				}
				stack.push(ch[i]);
			}
			else if (ch[i]=='+' || ch[i]=='-') {
				while(!stack.isEmpty() && (stack.peek()=='*'||stack.peek()=='/'
						||stack.peek()=='+'||stack.peek()=='-')) {
					sb.append(stack.pop());
				}
				stack.push(ch[i]);
			}
			else {
				sb.append(ch[i]);
			}
		}
		
		while (!stack.isEmpty()) sb.append(stack.pop());
		sb.append("\n");
		
		bw.write(sb.toString());
		bw.close();
	}

}
