package com.ssafy.day2.array;

public class BasicProblem_20{

	public static void main(String[] args) {
		char[][] chars = {{2,3,1,4},{1,'X',3,2},{3,4,'X','X'},{'X',4,1,5}
		};
		int x = 0;
		int [][] delta = {{1,0},{0,1},{-1,0},{0,-1}};
		for (int r = 0; r<4; r++) {
			for (int c = 0; c<4; c++) {
				if (chars[r][c]=='X') {
					for (int d = 0; d<4; d++) {
						int nr = r + delta[d][0];
						int nc = c + delta[d][1];
						if (0<=nr && nr<4 && 0<=nc && nc<4 && chars[nr][nc] !='X' && chars[nr][nc] !=0) {
							x+=chars[nr][nc];
							chars[nr][nc]=0;
						}
					}
				}
			}
		}
		System.out.println(x);
	}
}