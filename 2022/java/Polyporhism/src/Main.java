import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		System.out.print("�ѽ�:1,���:2");
		int input = scanner.nextInt();
		Food food;
		if (input == 1) {
			food = new Korean();
			food.show();
		}
		else if (input == 2) {
			food = new Western();
			food.show();
		}
	}
}
