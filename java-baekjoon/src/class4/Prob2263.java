package class4;

import java.util.*;
import java.io.*;

/*
 * 2263 : 트리의 순회 (시간 초과)
 */
public class Prob2263 {
	static int[] inOrder, postOrder;
	static int[] pos;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine()); // 10 ^ 5
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		inOrder = new int[n];
		pos = new int[n+1];
		for (int i = 0; i<n; i++) {
			inOrder[i] = Integer.parseInt(st.nextToken());
			pos[inOrder[i]] = i;
		}
		
		st = new StringTokenizer(br.readLine());
		postOrder = new int[n];
		for (int i = 0; i<n; i++) {
			postOrder[i] = Integer.parseInt(st.nextToken());
		}
		
		solve(0, inOrder.length-1, 0, postOrder.length-1);
	}
	
	static void solve(int stIn, int endIn, int stPost, int endPost) {
		if (stIn>endIn || stPost>endPost) return;
		
		int data = postOrder[endPost];
		int rootIdx = pos[data];
		int postIdx = stPost + (rootIdx - stIn) - 1;
		
		System.out.print(data + " ");
		
		solve(stIn, rootIdx-1, stPost, postIdx);
		solve(rootIdx+1, endIn, postIdx+1, endPost-1);
	}

}
