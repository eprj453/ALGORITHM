#include <iostream>
#include <queue>

using namespace std;

typedef struct Ans {
	int time;
	int last_cheese;
}Ans;

Ans cheese_melt(int cheese, int (*maps)[100], int n, int m) {
	Ans ans;
	int remain_cheese = cheese;
	int ans_time = 0;
	int last_cheese = 0;
	int dx[4] = {0, 1, 0, -1};
	int dy[4] = {1, 0, -1, 0};
	bool visited[100][100];
	while (true) {
		last_cheese = remain_cheese;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				visited[i][j] = false;
			}
		}

		queue < pair <int, int> > melt_cheese;
		int melt = 1;
		int idx = 0;
		bool result = false;
		for (int i = 0; i < n; i++) {
			if (result == true) break;
			for (int j = 0; j < m; j++) {
				if (maps[i][j] == 0) {
					queue< pair<int, int> > q;
					q.push(make_pair(i, j));
					while (q.size() > 0) {
						int x = q.front().first;
						int y = q.front().second;
						for (int k = 0; k < 4; k++) {
							if (x + dx[k] >= 0 && x +dx[k] < n && y + dy[k] >= 0 && y+dy[k] < m) {
								if (maps[x+dx[k]][y+dy[k]] == 1 && visited[x+dx[k]][y+dy[k]] == false) {
									visited[x+dx[k]][y+dy[k]] = true;
									melt_cheese.push(make_pair(x+dx[k], y+dy[k]));
								} else {
									if (maps[x+dx[k]][y+dy[k]] == 0 && visited[x+dx[k]][y+dy[k]] == false) {
										visited[x+dx[k]][y+dy[k]] = true;
										q.push(make_pair(x+dx[k], y+dy[k]));
									}
								}
							}
						}
						q.pop();
					}
					
					while (melt_cheese.size() > 0) {
						int x = melt_cheese.front().first;
						int y = melt_cheese.front().second;
						if (maps[x][y] == 1) {
							maps[x][y] = 0;
							remain_cheese -= 1;
						}
						melt_cheese.pop();
					}
					result = true;
					break;
				}
			}
		}
		ans_time++;
		ans.time = ans_time;
		ans.last_cheese = last_cheese;

		if (remain_cheese == 0) {
			break;
		} 

	}
	
	return ans;
}

int main() {

	int n, m, cheeses;
	cheeses = 0;
	cin >> n >> m;
	int maps[100][100];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			int temp;
			cin >> temp;
			if (temp == 1) {
				cheeses++;
			}
			maps[i][j] = temp;
		}
	}
	Ans ans;
	ans = cheese_melt(cheeses, maps, n, m);
	cout << ans.time << endl;
	cout << ans.last_cheese << endl;
}