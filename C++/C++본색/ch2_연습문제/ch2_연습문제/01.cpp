#include <iostream>
using namespace std;

int main(){
	// 1.
	double miles = 100;
	double MILE_TO_KILOMETER = 1.609;
	double kilometer;
	kilometer = miles * MILE_TO_KILOMETER;
	cout << kilometer << endl;

	// 2. 
	int score1 = 100, score2= 78, score3 = 78;
	int total;
	float average;
	total = score1 + score2 + score3;
	average = static_cast<float> (total)/ 3;
	cout << total << endl;
	cout << average << endl;
	
	// 3.
	cout << "사과가 " << 10 << "개 있다.\n";
	cout << "사과가 한 개에 " << 500 << "원이다\n";





}