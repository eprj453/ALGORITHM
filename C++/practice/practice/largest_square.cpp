#include <iostream>
using std::cin;
using std::cout;

int prize(int a, int b) {
	int a_prize[6] = {5000000, 3000000, 2000000, 500000, 300000, 100000};
	int b_prize[5] = {5120000, 2560000, 1280000, 640000, 320000};
	int total = 0;
	
	int a_temp = 0;
	if (a > 0 && a <= 21) {
		int p1 = 1;
		for (int i = 0; i < 6; i++) {
			a_temp += p1;
			if (a_temp >= a) {
				total += a_prize[i];
				break;
			} else {
				p1 += 1;
			}
		}
	}

	int b_temp = 0;
	if (b > 0 && b <= 31) {
		int p2 = 1;
		for (int i = 0; i < 5; i++) {
			b_temp += p2;
			if (b_temp >= b) {
				total += b_prize[i];
				break;
			} else {
				p2 *= 2;
			}
		}
	}
	return total;
}
int main(){
	int t;
	cin >> t;
	for (int tc = 1; tc < t+1; tc++) {
		int a, b;
		cin >> a;
		cin >> b;
		printf("%d\n", prize(a, b));
		
	}
	return 0;
}