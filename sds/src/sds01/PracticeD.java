package sds01;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/*
 * 1713 : 후보 추천하기
 * 백준에서 퍼블릭 클래스의 이름이 Main 이어야 함
 */
public class PracticeD {
	private static Queue<Integer> queue;
	private static int[] students;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		students = new int[101];
		
		try {
			int N = Integer.parseInt(br.readLine()); // 사진틀 개수
			int vote = Integer.parseInt(br.readLine()); // 추천 횟수
			queue = new LinkedList<>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < vote; i++) {
				int std = Integer.parseInt(st.nextToken());
				students[std] += 1;
				if(!queue.contains(std)) {
					if ( queue.size() < N ) {
						queue.add(std);
					}
					else if ( queue.size() >= N ) {
						// 삭제할 학생을 찾기
						int target = removeStudent();
						students[target] = 0;
						queue.remove(target);
						queue.add(std);
					}
				}
			}
			
			int[] arr = new int[N];
			int i = 0;
			for (Object o : queue.toArray()) {
				arr[i] = Integer.parseInt(o.toString());
				i++;
			}
			
			Arrays.sort(arr);
			for (Integer std: arr) {
				System.out.print(""+std+" ");
			}
			
			
			
			br.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public static int removeStudent() {
		int min = 1001;
		int ret = -1;
		for (Integer std : queue) {
			if (min > students[std]) {
				min = students[std];
				ret = std;
			}
		}
		return ret;
	}

}
