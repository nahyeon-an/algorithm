import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
 * 1920: 수 찾기
 * 처음 시도에 binary search가 아닌 A에서 하나씩 비교하여 큰 원소가 나오면 종료시키는 방법으로 구현
 * 시간 초과 나옴
 */

public class Main {
	private static int[] A;

	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			// Input
			int N = Integer.parseInt(br.readLine());
			A = new int[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				A[i] = Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(A);
			
			int M = Integer.parseInt(br.readLine());
			StringTokenizer st2 = new StringTokenizer(br.readLine());
			for (int i = 0; i < M; i++) {
				int target = Integer.parseInt(st2.nextToken());
				System.out.println(binarySearch(0, N, target));
			}
			
			br.close();	
			
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public static int binarySearch(int start, int end, int input) {
        int mid = (start + end )/2;
        
        if (mid >= end)
            return 0;
            
        if(A[mid] == input)
        {
            return 1;
        }else if (A[mid] < input)
        {
            return binarySearch(mid+1, end, input);
        }else {
            return binarySearch(start, mid, input);
        }
    }
}
