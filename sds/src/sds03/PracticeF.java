package sds03;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/*
 * 6416 : 트리인가?
 */
public class PracticeF {
	private static int tc;
	private static Map<Integer, Integer> map;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = null;
		map = new HashMap<>();
		tc = 0;
		while(true) {
			s = br.readLine().split(" ");
			int len = s.length;
			int i = 0;
			while(i < len-1) {
				if (s[i].equals("")) {
					i++;
				}
				else {
					if (s[i].equals("0")&&s[i+1].equals("0")) {
						boolean flag = true;
						if (map.size() == 0) flag = false;
						for (int v:map.values()) {
							if (v > 1) {
								flag = false;
							}
						}
						if (flag) {
							System.out.println("Case "+(++tc)+" is a tree.");
						}
						else {
							System.out.println("Case "+(++tc)+" is not a tree.");
						}
						map.clear();
					}
					else if (s[i].equals("-1")&&s[i+1].equals("-1")) {
						System.out.println("exit");
						return;
					}
					else {
						// s[i] -> s[i+1]
						int s1 = Integer.parseInt(s[i]);
						int s2 = Integer.parseInt(s[i+1]);
						if (!map.containsKey(s1))
							map.put(s1, 0);
						if (!map.containsKey(s2))
							map.put(s2, 1);
						else {
							map.put(s2, map.get(s2)+1);
						}
					}
					i = i+2;
				}
			}
		}
	}
}
