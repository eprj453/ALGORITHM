#include <iostream>
using namespace std;
int main() {
	char string[30] = "computer programming is very interesting!!";
	int i = 0;

	cout << string << endl;

	for (i = 0; string[i] != '\0'; i++) {
		cout << string[i];
	}

	cout << endl;
}