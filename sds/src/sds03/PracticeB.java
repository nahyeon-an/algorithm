package sds03;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/*
 * 10845 : ť
 */
public class PracticeB {
	private static int N;
	private static Queue<Integer> q;
	private static int back;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		q = new LinkedList<>();
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
			if (arg != -1) {
				q.add(arg);
				back = arg;
			}
		}
		else if (cmd.equals("front")) {
			if (!q.isEmpty()) {
				System.out.println(q.peek());
			}
			else {
				System.out.println(-1);
			}
		}
		else if (cmd.equals("back")) {
			if (!q.isEmpty()) {
				System.out.println(back);
			}
			else {
				System.out.println(-1);
			}
		}
		else if (cmd.equals("pop")) {
			if (!q.isEmpty()) {
				System.out.println(q.poll());
			}
			else {
				System.out.println(-1);
			}
		}
		else if (cmd.equals("size")) {
			System.out.println(q.size());
		}
		else if (cmd.equals("empty")) {
			if (q.isEmpty()) {
				System.out.println(1);
			}
			else {
				System.out.println(0);
			}
		}
		else return;
	}

}
