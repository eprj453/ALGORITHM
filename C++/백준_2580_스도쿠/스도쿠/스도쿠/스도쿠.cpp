#include <iostream>
#include <vector>
using namespace std;
int sudoku[9][9];

vector < pair <int, int> > column_check() {
	vector <pair <int, int>> temp;
	return temp;
} 

vector < pair <int, int> > row_check() {
	vector <pair <int, int>> temp;
	return temp;
} 

vector < pair <int, int> > square_check() {
	vector <pair <int, int>> temp;
	return temp;
} 

int main(){
	int num;
	vector < vector <pair <int, int>> > blanks;
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> num;
			sudoku[i][j] = num;
		}
	}

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			if (sudoku[i][j] == 0) {
				
			}
		}
	}
}