package com.ssafy.day2.person;

public class Person {
	// 멤버 변수
	String name;
	boolean isHungry;
	int age;
	
	// 메서드
	void eat() {
		System.out.println("냠냠..");
		isHungry = false;
	}
	
	void work() {
		System.out.println("열심.....");
		isHungry = true;
	}
}
