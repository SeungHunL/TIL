package com.ssafy.day2.array;

import java.util.Arrays;

public class BasicProblem_15{

	public static void main(String[] args) {
		char[][] chars = {{'C','A','A'},{'C','C','B'},{'B','A','B'},{'C','C','C'}
		};
		for(char[] carray:chars) {
			for(char c :carray) {
				System.out.print(c);
			}
			System.out.println();
		}
		System.out.println(Arrays.toString(chars));
		System.out.println(Arrays.deepToString(chars));
	}
}