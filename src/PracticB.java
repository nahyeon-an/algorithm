import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/*
 * 3055 : 탈출
 */
public class PracticB {
	private static char[][] map;
	private static boolean[][] visited;
	private static int[] dx = {1,-1,0,0};
	private static int[] dy = {0,0,1,-1};
	private static Queue<Pair> q1; // 물
	private static Queue<Pair> q2; // 고슴도치
	private static int ans = 0; // 시간
	
	

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
					if (map[i][j] == 'S') { // 고슴도치 위치
						q2.add(new Pair(i, j));
					}
					else if (map[i][j] == '*') { // 물이 차 있는 곳
						q1.add(new Pair(i, j));
					}
				}
			}
			
			// 물과 고슴도치는 돌을 통과할 수 없다.
			// 고슴도치는 물로 차있는 구역으로 이동할 수 없고
			// 물도 비버의 소굴로 이동할 수 없다.
			
			// 고슴도치는 매 분 마다 상하좌우로 움직임
			// 물도 매 분 마다 상하좌우로 확장
						
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
			// map 을 벗어나지 않으면
			if ((nx > -1) && (nx < map[0].length)
					&& (ny > -1) && (ny < map.length)) {
				// map 에서 이동가능한 자리인지 (.)인지
				if (map[ny][nx] == '.') {
					map[ny][nx] = '*';
				}
				else if (map[ny][nx] == 'S') {
					System.out.println("KAKTUS");
					return; // 프로그램 종료
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
				// 이동가능
				if (map[my][mx] == '.') {
					map[ay][ax] = '.';
					map[my][mx] = 'S';
					bfs(); // 다시 호출? 해야하는데..
					map[ay][ax] = 'S';
					map[my][mx] = '.';
				}
				else if (map[my][mx] == 'D') {
					return; // 종료
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
