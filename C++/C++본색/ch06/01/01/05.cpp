#include <iostream>
using namespace std;
int main() {
	int score[3] = {100, 90, 80};

	cout << "score[0]�� �ּ� : " << &score[0] << endl;
	cout << "score[1]�� �ּ� : " << &score[0] << endl;
	cout << "score[2]�� �ּ� : " << &score[0] << endl;
	
	cout << "==============================================" << endl;

	for (int i = 0; i < 3; i++) {
		cout << "score[" << i << "]�� �ּ� : " << &score[i]<< endl;
	}

	cout << "==============================================" << endl;

	cout << "score[0]�� �ּ� : " << score << endl;
	cout << "score[1]�� �ּ� : " << score+1 << endl;
	cout << "score[2]�� �ּ� : " << score+2 << endl;

	cout << "==============================================" << endl;

	for (int i = 0; i < 3; i++) {
		cout << "score[" << i << "]�� �ּ� : " << score + i<< endl;
	}
	return 0;
}