import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/*
 * 1713 : �ĺ� ��õ�ϱ�
 * ���ؿ��� �ۺ� Ŭ�����̸��� Main �̾�� ��
 */
public class PracticeD {
	private static Queue<Integer> queue;
	private static int[] students;

	public static void main(String[] args) {
		// �Է�
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		students = new int[101];
		
		try {
			int N = Integer.parseInt(br.readLine()); // ����Ʋ ����
			int vote = Integer.parseInt(br.readLine()); // ��õ Ƚ��
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
						// ������ �л��� ã��
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
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		// ��õ ���� �л��� �ݵ�� ����Ʋ�� �Խ�
		// ����Ʋ�� �� ���ִ� -> (1) ��õ ���� ���� �л� ���� ���� (2) ���� ������ ���� / ���ο� �л� �Խ�
		// ����Ʋ�� �ִ� �л� -> ��õ Ƚ�� ����
		// ����Ʋ���� ���� -> ��õ Ƚ�� = 0
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
