#include <iostream>
#include <stdio.h>
using namespace std;
int main() {
	int c, n;
	cin >> c;
	double tmp;
	for (int tc = 1; tc < c+1; tc++) {
		cin >> n;
		double coor[10];
		double weight[10];
		double ans[9];
		double m = 1 / pow(10.0, 11.0);
		for (int i = 0; i < n*2; i++) {
			cin >> tmp;
			if (i < n) {
				coor[i] = tmp;
			} else {
				weight[i-n] = tmp;
			}
		}

		//int low = 0, high = 1;
		for (int i = 0; i < n-1; i++) {
			double coor_low = coor[i];
			double coor_high = coor[i+1];
			int t = 0;
			while (coor_low <= coor_high) {
				if (t > 1000) break;
				double balance = 0;
				double coor_mid = (coor_low + coor_high) / 2;
				//printf("coor_mid : %.10lf\n", coor_mid);
				for (int k = i; k > -1; k--) {
					balance += (weight[k] / ((coor_mid - coor[k]) * (coor_mid - coor[k])));
				}

				for (int k = i+1; k < n; k++) {
					balance -= (weight[k] / ((coor_mid - coor[k]) * (coor_mid - coor[k])));
				}
				// balance�� ������� ���������� ġ��� ��.
				printf("%.12f\n", balance);
				if (balance < 0) { // ���������� ġ������
					coor_high = coor_mid;
				} else {
					coor_low = coor_mid; // �������� ġ������
				}
				ans[i] = coor_mid;
				if (0 <= balance && balance < m) break;
				t++;
			}
			cout << "t : " << t << endl;
		}

		cout << "#"<< tc << " ";
		for (int i = 0; i < n-1; i++) {
			printf("%.10f", ans[i]);
			cout << " ";
		}
		cout << endl;
	}
}