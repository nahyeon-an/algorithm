package class4;

import java.util.*;
import java.io.*;

/*
 * 2263 : 트리의 순회 (시간 초과)
 */
public class Prob2263 {
	static int[] inOrder, postOrder;
	static Tree tree;
	static Node root;
	static int[] pos;
	
	static class Node {
		int data;
		Node left, right;
		
		Node (int data) {
			this.data = data;
		}
	}
	
	static class Tree {
		Node root;
		
		Tree (int data, int left, int right) {
			root = new Node(data);
			if (left > 0)
				root.left = new Node(left);
			if (right > 0)
				root.right = new Node(right);
		}
		
		void add (int data, int left, int right) {
			next(root.left, data, left, right);
			next(root.right, data, left, right);
		}
		
		void next(Node n, int data, int left, int right) {
			if (n == null) return;
			
			if (n.data == data) {
				if (left > 0) n.left = new Node(left);
				if (right > 0) n.right = new Node(right);
			}
			else {
				next(n.left, data, left, right);
				next(n.right, data, left, right);
			}
		}
		
		void preOrder(Node n) {
			System.out.print(n.data + " ");
			if (n.left != null) preOrder(n.left);
			if (n.right != null) preOrder(n.right);
		}
	}

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
		
		func(inOrder, postOrder);
		
		tree.preOrder(tree.root);
		
		System.out.println("\n-------------");
		
		solve(0, inOrder.length-1, 0, postOrder.length-1);
	}
	
	static void solve(int stIn, int endIn, int stPost, int endPost) {
		if (stIn>endIn || stPost>endPost) return;
		
		int data = postOrder[endPost];
		int rootIdx = pos[data];
		// 위치 계산
	
		System.out.print("("+data+","+rootIdx+") ");
		solve(stIn, rootIdx-1, stPost, rootIdx-1);
		solve(rootIdx+1, endIn, rootIdx, endPost-1);
	}
	
	static void func(int[] in, int[] post) {
		int ilen = in.length;
		int plen = post.length;
		
		if (ilen == 0 || plen==0) return;
		
		int data = post[plen-1];
		
		int idx = 0;
		for (int i = 0; i<=ilen; i++) {
			if (in[i] == data) {
				idx = i;
				break;
			}
		}
		
		int left = 0;
		if (idx >= 1)
			left = post[idx-1];
		
		int right = 0;
		if (plen >= 2)
			right = post[plen-2];
		
		if (left == right) right = 0;
				
		if (tree != null) tree.add(data, left, right);
		else tree = new Tree(data, left, right);
		
		int[] l = new int[idx];
		int[] r = new int[idx];
		for (int i = 0; i<=idx-1; i++) {
			l[i]=in[i];
			r[i]=post[i];
		}
		
		func(l, r);
		
		l = new int[ilen-idx-1];
		int j = 0;
		for (int i = idx+1; i<ilen; i++) {
			l[j++] = in[i];
		}
		
		r = new int[plen-idx-1];
		j = 0;
		for (int i = idx; i<=plen-2; i++) {
			r[j++] = post[i];
		}

		func(l, r);
	}

}
