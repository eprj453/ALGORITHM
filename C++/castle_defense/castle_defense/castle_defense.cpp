#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
	int n, m, d;
	cin >> n;
	cin >> m;
	cin >> d;
	vector <vector <int>> maps (n, vector <int> (m, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int temp;
			cin >> temp;
			maps[i][j] = temp;
		}
	}



	return 0;
}