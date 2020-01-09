#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

struct my_info {int x, y, d;};


int min(int arg1, int arg2) {
	if (arg1 > arg2) {
		return arg2;
	} else {
		return arg1;
	}
}

int main(){
	int dx[4] = {-1, 0, 1, 0};
	int dy[4] = {0, -1, 0, 1};
	

	int t;
	cin >> t;
	for (int tc = 1; tc < t+1; tc++) {
		int w, h;
		cin >> w >> h;
		char maps[1000][1000];
		bool visited[1000][1000];
		queue<pair <int, int>> fires;
		my_info me[1000 * 1000];
		for (int i = 0; i < w; i++) {
			for (int j = 0; j < h; j++) {
				visited[i][j] = false;
			}
		}

		int min_distance = 1000* 1000;
		string ans = "";
		int idx = 0;
		char temp;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> temp;
				if (temp == '*') {
					fires.push(make_pair(i, j));
				} 
				else if (temp == '@') {
					my_info mi;
					mi.x = i;
					mi.y = j;
					mi.d = 0;
					me[idx++] = mi;
				}
				maps[i][j] = temp;
			}
		}
		int me_idx = idx;
		while (me_idx > 0) {
			if (fires.size() > 0) {
				queue<pair <int, int>> new_fires;
				while (fires.size() > 0) {
					int x = fires.front().first;
					int y = fires.front().second;
					for (int k = 0; k < 4; k++) {
						if (0 <= x + dx[k] && h > x + dx[k] && 0 <= y + dy[k] && w > y + dy[k]) {
							if (maps[x + dx[k]][y + dy[k]] != '#' && visited[x + dx[k]][y + dy[k]] == false) {
								maps[x + dx[k]][y + dy[k]] = '*';
								visited[x + dx[k]][y + dy[k]] = true;
								new_fires.push(make_pair(x + dx[k], y + dy[k]));
							}
						}
					}
					fires.pop();
				}
				fires = new_fires;
			}
			for (my_info info : me) {
				int x = info.x;
				int y = info.y;
				int d = info.d;

				if (x == 0 || y == 0 || x == h - 1 || y == w - 1) {
					min_distance = min(min_distance, d);
				}
			}

			my_info new_me[1000*1000];
			int new_idx = 0;
			for (my_info info : me) {
				int x = info.x;
				int y = info.y;
				int d = info.d;
				for (int k = 0; k < 4; k++) {
					if (0 <= x + dx[k] && h > x + dx[k] && 0 <= y + dy[k] && w > y + dy[k]) {
						if (maps[x + dx[k]][y + dy[k]] == '.') {
							maps[x + dx[k]][y + dy[k]] = '@';
							my_info mi;
							mi.x = x + dx[k];
							mi.y = y + dy[k];
							mi.d = d + 1;
							new_me[new_idx++] = mi;
							//new_me.resize((int)new_me.size() + 1);
							//new_me.push_back(mi);
						}
					}
				}
			}
			me_idx = new_idx;
			me = new_me;
		}

		

		
	if (min_distance == 1000 * 1000) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << min_distance << endl;
	}
}
}
