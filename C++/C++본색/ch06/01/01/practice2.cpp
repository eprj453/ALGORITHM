#include <iostream>
using namespace std;
int main() {
	char jumin[30] = {0,};
	char year[5] = {0,};
	//char month[3];
	//char day[3];
	cout << "주민번호 입력 : ";
	cin >> jumin;

	if (jumin[6] != '-') {
		cout << "입력오류" << endl;
	} else {
		if (jumin[7] == '1' || jumin[7] == '2') {
			strcpy_s(year, "19");
		} else {
			strcpy_s(year, "20");
		}
	}

	strncat_s(year, _countof(year) jumin, 2);

	cout << year << endl;
}