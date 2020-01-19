#include <iostream>
#include <vector>
using namespace std;

int main() {
	int	n;
	int locs[10];
	bool connect[11][11];
	int temp;
	//vector <vector <int>> connect;
	//int arr[10][10];
	cin >> n;
	for (int i = 0; i < n+1; i++) {
		if (i == 0) {
			for (int j = 0; j < n; j++) {
				cin >> temp; 
				locs[j] = temp; 
			} 
		} else {
			cin >> temp;
			int temp2;
			for (int j = 1; j < temp+1; j++) {
				cin >> temp2;
				connect[temp2][j] = true;
				connect[j][temp2] = true;
			}
		}
	}

	for (int i = 0; i < 11; i++) {
		for (int j = 0; j < 11; j++) {
			cout << connect[i][j] << " ";
		}
		cout << endl;
	}
}