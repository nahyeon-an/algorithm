package sds03;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * 1991 : 트리 순회
 */
public class PracticeC {
	private static int N;
	private static Tree tree;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		String first = br.readLine().replaceAll(" ", "");
		tree = new Tree(first.charAt(0), first.charAt(1), first.charAt(2));
		
		for (int i = 1; i < N; i++) {
			String s = br.readLine().replaceAll(" ", "");
			tree.add(s.charAt(0), s.charAt(1), s.charAt(2));
		}
		
		br.close();
		
		tree.preOrder(tree.root);
		System.out.println();
		tree.inOrder(tree.root);
		System.out.println();
		tree.postOrder(tree.root);
	}
	
}

class Node {
	char data;
	Node left;
	Node right;
	
	public Node(char data) {
		this.data = data;
	}
}

class Tree {
	Node root;
	
	// Ʈ���� ��Ʈ �ʱ�ȭ
	public Tree(char data, char left, char right) {
		root = new Node(data);
		
		if (left != '.')
			root.left = new Node(left);
		if (right != '.')
			root.right = new Node(right);
	}
	
	public void add(char data, char left, char right) {
		next(root.left, data, left, right);
		next(root.right, data, left, right);
	}
	
	public void next(Node node, char data, char left, char right) {
		if (node == null) return;
		
		if (node.data == data) {
			if (left != '.')
				node.left = new Node(left);
			if (right != '.')
				node.right = new Node(right);
		}
		else {
			next(node.left, data, left, right);
			next(node.right, data, left, right);
		}
	}
	
	public void preOrder(Node n) {
		System.out.print(n.data);
		if (n.left != null)
			preOrder(n.left);
		if (n.right != null)
			preOrder(n.right);
	}
	
	public void inOrder(Node n) {
		if (n.left != null)
			inOrder(n.left);
		
		System.out.print(n.data);
		
		if (n.right != null)
			inOrder(n.right);
	}
	
	public void postOrder(Node n) {
		if (n.left != null)
			postOrder(n.left);
		
		if (n.right != null)
			postOrder(n.right);
		
		System.out.print(n.data);
	}
}
