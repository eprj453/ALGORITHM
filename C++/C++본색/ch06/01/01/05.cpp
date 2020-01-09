#include <iostream>
using namespace std;
int main() {
	int score[3] = {100, 90, 80};

	cout << "score[0]狼 林家 : " << &score[0] << endl;
	cout << "score[1]狼 林家 : " << &score[0] << endl;
	cout << "score[2]狼 林家 : " << &score[0] << endl;
	
	cout << "==============================================" << endl;

	for (int i = 0; i < 3; i++) {
		cout << "score[" << i << "]狼 林家 : " << &score[i]<< endl;
	}

	cout << "==============================================" << endl;

	cout << "score[0]狼 林家 : " << score << endl;
	cout << "score[1]狼 林家 : " << score+1 << endl;
	cout << "score[2]狼 林家 : " << score+2 << endl;

	cout << "==============================================" << endl;

	for (int i = 0; i < 3; i++) {
		cout << "score[" << i << "]狼 林家 : " << score + i<< endl;
	}
	return 0;
}