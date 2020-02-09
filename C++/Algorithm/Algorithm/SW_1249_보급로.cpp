#include <iostream>
#include <stack>
#include <string>

using namespace std;
int ans;
int n;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void search(stack <pair <int, int>> stk, int cost, int maps[100][100], bool visited[100][100]) {
	while (stk.size() > 0) {
		int x = stk.top().first;
		int y = stk.top().second;

		if (cost >= ans) return;
		for (int k = 0; k < 4; k++) {
			
			if (0 <= x + dx[k] && x + dx[k] < n && 0 <= y + dy[k] && y + dy[k] < n && visited[x+dx[k]][y+dy[k]] == false && maps[x+dx[k]][y+dy[k]] != 0) {
				visited[x+dx[k]][y+dy[k]] = true;
				stk.push(make_pair(x + dx[k], y + dy[k]));
				search(stk, cost + maps[x+dx[k]][y+dy[k]], maps, visited);
				visited[x+dx[k]][y+dy[k]] = false;
				stk.pop();
			}
		}
		stk.pop();
	}
	return;
}

int main() {
	int t;
	cin >> t;
	for (int tc = 1; tc < t+1; tc++) {
		ans = 10000;
		string temp;
		cin >> n;
		int maps[100][100];

		for (int i = 0; i < n; i++) {
			cin >> temp;
			for (int j = 0; j < n; j++) {
				maps[i][j] = temp[j] - '0';
			}
		}
		bool visited[100][100] = {false,};
		visited[0][0] = true;
		stack <pair <int, int>> stk;
		stk.push(make_pair(0, 0));
		search(stk, maps[0][0], maps, visited);

		cout << "#" << tc << " " << ans << endl;
	}
	return 0;
}