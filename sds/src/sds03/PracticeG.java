package sds03;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

/*
 * 5639 : 이진 검색 트리
 */
public class PracticeG {
	private static ArrayList<Integer> nums;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			String s = br.readLine();
			if(s == "") {
				break;
			}
			else {
				nums.add(Integer.parseInt(s));
			}
		}
		br.close();
				
		function(nums);
	}

	public static void function(ArrayList<Integer> arr) {
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
}

class Tree2 {
	Node2 root;
	
	public Tree2(int data, int left, int right) {
		root.data = data;
		if (left > 0) 
			root.left = new Node2(left);
		if (right > 0)
			root.right = new Node2(right);
	}
}
