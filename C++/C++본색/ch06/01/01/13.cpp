#include <iostream>
using namespace std;
int main() {
	char string[30] = "";
	cin >> string;

	char copy_string[30] = "";

	for (int i = 0; string[i] != '\0'; i++) {
		copy_string[i] = string[i];	
	}


	cout << "string : " << string << endl; 


	cout << "copy_string : " << copy_string << endl;






}