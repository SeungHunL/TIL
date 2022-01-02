package com.ssafy.day2.person;

public class Persontest {

	public static void main(String[] args) {
		Person p1 = new Person();
		p1.age = 3;
		System.out.println(p1.age);
		System.out.println(p1.isHungry);
		System.out.println(p1.name);
		p1.eat();
		p1.work();
	}

}
