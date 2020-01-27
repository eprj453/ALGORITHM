#include <iostream>
using namespace std;
int n, m;
int main() {
	int t, tmp;
	cin >> t;
	int chocolate[50][50];
	int cut[49][49] = {false,};
	for (int tc = 1; tc < t+1; tc++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> tmp;
				chocolate[i][j] = tmp;
			}
		}
		
	}
}