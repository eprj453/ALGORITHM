#include <iostream>
#include <vector>
using namespace std;

int main() { 
	int n, k;
	cin >> n >> k;
	pair<int, int> things[100];
	//vector <pair <int, int>> things;
	for (int i = 0; i < n; i++) {
		int w, v;
		things[i] = make_pair(w, v);
		//things.push_back(make_pair(w, v));
	}

	int dp[101][100001];

	for (int i = 0; i < n + 1; i++) { // 보석 갯수
		for (int j = 0; j < k + 1; k++) { // 무게
			int w = things[i].first;
			int v = things[i].second;
			if (i == 0 || j == 0) {
				dp[i][j] == 0;
			}
			else if (w > k) {
				dp[i][j] = dp[i - 1][j];
			}
			else {
				dp[i][j] = max(dp[i - 1][j - w], dp[i - 1][j]);
			}
		}
	}

	cout << dp[n][k] << endl;
}