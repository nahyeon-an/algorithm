import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/*
 * 3055 : Ż��
 */
public class PracticB {
	private static char[][] map;
	private static boolean[][] visited;
	private static int[] dx = {1,-1,0,0};
	private static int[] dy = {0,0,1,-1};
	private static Queue<Pair> q1; // ��
	private static Queue<Pair> q2; // ����ġ
	private static int ans = 0; // �ð�
	
	

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		try {
			String[] temp = br.readLine().split(" ");
			int R = Integer.parseInt(temp[0]);
			int C = Integer.parseInt(temp[1]);
			map = new char[R][C];
			visited = new boolean[R][C];
			q1 = new LinkedList<>();
			q2 = new LinkedList<>();
			for (int i = 0; i < R; i++) {
				String[] row = br.readLine().split("");
				for (int j = 0; j < C; j++) {
					map[i][j] = row[j].charAt(0);
					if (map[i][j] == 'S') { // ����ġ ��ġ
						q2.add(new Pair(i, j));
					}
					else if (map[i][j] == '*') { // ���� �� �ִ� ��
						q1.add(new Pair(i, j));
					}
				}
			}
			
			// ���� ����ġ�� ���� ����� �� ����.
			// ����ġ�� ���� ���ִ� �������� �̵��� �� ����
			// ���� ����� �ұ��� �̵��� �� ����.
			
			// ����ġ�� �� �� ���� �����¿�� ������
			// ���� �� �� ���� �����¿�� Ȯ��
						
			br.close();
			
			System.out.println(ans);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	public static void bfs() {
		
		ans += 1;
		
		Pair water = q1.poll();
		int wx = water.x;
		int wy = water.y;
		
		// water
		for (int i = 0; i < 4; i++) {
			int nx = wx + dx[i];
			int ny = wy + dy[i];
			// map �� ����� ������
			if ((nx > -1) && (nx < map[0].length)
					&& (ny > -1) && (ny < map.length)) {
				// map ���� �̵������� �ڸ����� (.)����
				if (map[ny][nx] == '.') {
					map[ny][nx] = '*';
				}
				else if (map[ny][nx] == 'S') {
					System.out.println("KAKTUS");
					return; // ���α׷� ����
				}
			}
		}
		
		Pair animal = q2.poll();
		// animal
		int ax = animal.x;
		int ay = animal.y;
		for (int i = 0; i < 4; i++) {
			int mx = ax + dx[i];
			int my = ay + dy[i];
			
			if ((mx > -1) && (mx < map[0].length)
					&& (my > -1) && (my < map.length)) {
				// �̵�����
				if (map[my][mx] == '.') {
					map[ay][ax] = '.';
					map[my][mx] = 'S';
					bfs(); // �ٽ� ȣ��? �ؾ��ϴµ�..
					map[ay][ax] = 'S';
					map[my][mx] = '.';
				}
				else if (map[my][mx] == 'D') {
					return; // ����
				}
			}
		}
	}

}

class Pair {
	public int x;
	public int y;
	Pair(int y, int x){
		this.y = y; // row
		this.x = x; // col
	}
	
	public String toString() {
		return "["+y+"]["+x+"]";
	}
}
