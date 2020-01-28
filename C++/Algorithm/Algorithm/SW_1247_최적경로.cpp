#include <iostream>
using namespace std;

int min_distance;

void findDistance(int n, bool visited[10], int distance) {
	for (int k = 1; k < n-1; k++) {
		if (visited[k] == false) {
			visited[k] = true;
			distance 
		}
	}
}
int main() {
	int t;
	for (int tc = 1; tc < t+1; tc++) {
		int n;
		cin >> n;
		int home[2];
		int company[2];
		int customers[10][2];
		for (int i = 0; i < n+2; i++) {
			int x, y;
			cin >> x >> y;
			if (i == 0) {
				home[0] = x;
				home[1] = y;
			} else if (i == 1) {
				company[0] = x;
				company[1] = y;
			} else {
				customers[i-2][0] = x;
				customers[i-2][1] = y;
			}
		}
		min_distance = 1000;

	}
}