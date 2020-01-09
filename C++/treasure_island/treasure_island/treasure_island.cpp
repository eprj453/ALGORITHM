#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int ans;
int w, h;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
char maps[50][50];

struct info {
	int x;
	int y;
	int d;
};

void find(int x, int y) {
	bool visited[50][50];
	queue <info> q;
	info newInfo;
	newInfo.x = x;
	newInfo.y = y;
	newInfo.d = 0;
	q.push(newInfo);
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			visited[i][j] = false;
		}
	}

	while (q.size() > 0) {
		int xx = q.front().x;
		int yy = q.front().y;
		int dd = q.front().d;


		for (int k = 0; k < 4; k++) {
			if (xx + dx[k] >= 0 && xx + dx[k] < h && yy + dy[k] >= 0 && yy + dy[k] < w) {
				if (maps[xx + dx[k]][yy+dy[k]] == 'L' && visited[xx + dx[k]][yy+dy[k]] == false) {
					visited[xx + dx[k]][yy+dy[k]] = true;
					info temp;
					temp.x = xx + dx[k];
					temp.y = yy + dy[k];
					temp.d = dd + 1;
					if (temp.d > ans) {
						ans = temp.d;
					}
					q.push(temp);
				}
			}
		}
		q.pop();
	}

}


int main(){
	ans = 0;
	
	char letter;
	cin >> h >> w;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			cin >> letter;
			maps[i][j] = letter;
		}
	}

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (maps[i][j] == 'L') {
				find(i, j);
			}
		}
	}

	cout << ans << endl;

}
