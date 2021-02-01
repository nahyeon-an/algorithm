package sds03;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

/*
 * 5639 : 이진 검색 트리
 */
public class PracticeG {
	private static ArrayList<Integer> nums;
	private static Tree2 tree;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		nums = new ArrayList<>();
		String s = "";
		while((s=br.readLine())!=null && s.length()!=0) {
			nums.add(Integer.parseInt(s));
		}
		br.close();
						
		function(nums);
		
		tree.postOrder(tree.root);
	}

	public static void function(ArrayList<Integer> arr) {
		if (arr.size() == 0) return;
		int root = arr.get(0);
		int size = arr.size();
		ArrayList<Integer> left = new ArrayList<>();
		ArrayList<Integer> right = new ArrayList<>();
		
		for (int i = 1; i < size; i++) {
			int val = arr.get(i);
			if (val > root) {
				right.add(val);
			}
			else {
				left.add(val);
			}
		}
				
		int l = -1, r = -1;
		if (left.size() > 0) {
			l = left.get(0);
		}
		if (right.size() > 0) {
			r = right.get(0);
		}
		
		if(tree != null) {
			tree.add(root, l, r);
		}
		else {
			tree = new Tree2(root, l, r);
		}
		
		function(left);
		function(right);
	}
}

class Node2 {
	int data;
	Node2 left;
	Node2 right;
	
	public Node2(int data) {
		this.data = data;
	}
	
	public String toString() {
		return "" + this.data;
	}
}

class Tree2 {
	Node2 root;
	
	public Tree2(int data, int left, int right) {
		root = new Node2(data);
		if (left > 0) 
			root.left = new Node2(left);
		if (right > 0)
			root.right = new Node2(right);
	}
	
	public void add(int data, int left, int right) {
		next(root.left, data, left, right);
		next(root.right, data, left, right);
	}
	
	public void next(Node2 node, int data, int left, int right) {
		if (node == null) return;
		
		if (node.data == data) {
			if (left != -1)
				node.left = new Node2(left);
			if (right != -1)
				node.right = new Node2(right);
		}
		else {
			next(node.left, data, left, right);
			next(node.right, data, left, right);
		}
	}
	
	public void postOrder(Node2 n) {
		if (n.left != null)
			postOrder(n.left);
		
		if (n.right != null)
			postOrder(n.right);
		
		System.out.println(n.data);
	}
}
