#include <iostream>
using namespace std;
int main() {

	char ch = 'y', name[30] = "GABDOL";

	cout <<  hex << (int)&ch << endl;

	cout << hex << (int)name << endl;

	cout << hex << (int)&name[0] << endl;

}