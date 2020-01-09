#include <iostream>
using namespace std;

int main(){

	char Name[50];
	int FunResult;
	FunResult = strcpy_s(Name, "Ã¤Ä¡¼ö");

	//cout << FunResult << endl;
	//cout << Name << endl;

	int a = 100;
	int * pa;

	pa = &a;

	cout << pa << endl;
	cout << &a << endl;
	cout << *pa << endl;

	return 0;
}