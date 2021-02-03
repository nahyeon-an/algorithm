package sds08;

public class Matrix {

	public static void main(String[] args) {
		int n; // 행렬개수
		
		for (int len = 2; len<=n; len++) { // 쪼개는 길이
			for (int i = 1; i <= n - len+1; i++) {
				int j = i +len-1;
				dp[i][j] = INF;
				for (int k = i; k<=j-1; k++) {
					int temp = dp[i][k] + dp[k+1][j] + mat[i][0] * mat[k][1] * mat[j][1];
					dp[i][j] = Math.min(dp[i][j], temp);
				}
			}
		}
	}
	
	// st ~ end 계산하는데 걸리는 최소시간
	static int dfs(int st, int end) { // 0, n-1 (1, n)
		
		int ret = 999999999;
		for (int i = st; i<end; i++) {
			dp[st][end] = Math.min(dfs(st, i) + dfs(i+1, end) + mat[st][0] * mat[i][1] * mat[end][1]);
		}
		
		return dp[st][end];
	}
}
