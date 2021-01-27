package sds03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/*
 * 10828 : Ω∫≈√
 */
public class PracticeA {
	private static int N;
	private static Stack<Integer> st;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		st = new Stack<>();
		for (int i = 0; i < N ; i++) {
			String[] s = br.readLine().split(" ");
			String cmd;
			int arg;
			
			if (s.length == 1) {
				cmd = s[0];
				arg = -1;
			}
			else {
				cmd = s[0];
				arg = Integer.parseInt(s[1]);
			}
			execute(cmd, arg);
		}
		br.close();
	}
	
	public static void execute(String cmd, int arg) {
		if (cmd.equals("push")) {
			if (arg != -1) st.push(arg);
		}
		else if (cmd.equals("top")) {
			if (!st.isEmpty()) {
				System.out.println(st.peek());
			}
			else {
				System.out.println(-1);
			}
		}
		else if (cmd.equals("pop")) {
			if (!st.isEmpty()) {
				System.out.println(st.pop());
			}
			else {
				System.out.println(-1);
			}
		}
		else if (cmd.equals("size")) {
			System.out.println(st.size());
		}
		else if (cmd.equals("empty")) {
			if (st.isEmpty()) {
				System.out.println(1);
			}
			else {
				System.out.println(0);
			}
		}
		else return;
	}

}
