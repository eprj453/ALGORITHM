#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int maps[10][10];
int visited[10][10] = {false,};
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};
int bridge_len;
int max(int x, int y) {
	return x > y ? x : y;
}

int min(int x, int y) {
	return x > y ? y : x;
}

int n, m;

void findBridge(int i, int j) {
	cout << "---------------함수 호출-----------------" << endl;
	int top_max = i;
	int bottom_max = i;
	int left_max = j;
	int right_max = j;
	queue <pair<int, int>> q;
	q.push(make_pair(i, j));
	visited[i][j] = true;
	while (q.size() > 0) {
		int x = q.front().first;
		int y = q.front().second;
		for (int k = 0; k < 4; k++) {
			if (0 <= x + dx[k] && x + dx[k] < n && 0 <= y + dy[k] && y + dy[k] < m) {
				if (maps[x+dx[k]][y+dy[k]] == 1 && visited[x+dx[k]][y+dy[k]] == false) {
					q.push(make_pair(x + dx[k], y + dy[k]));
					top_max = min(i, x + dx[k]);
					bottom_max = max(i, x + dx[k]);
					left_max = min(j, y + dy[k]);
					right_max = max(j, y + dy[k]);
					visited[x+dx[k]][y+dy[k]] = true;
				}
			}
		}
		q.pop();
	}

	vector <pair<int, int>> top;
	vector <pair<int, int>> bottom;
	vector <pair<int, int>> left;
	vector <pair<int, int>> right;
	vector < vector <pair<int, int>>> island;
	for (int k = left_max; k < right_max+1; k++) {
		top.push_back(make_pair(top_max, k));
	}
	
	for (int k = top_max; k < bottom_max+1; k++) {
		right.push_back(make_pair(k, right_max));
	}
	for (int k = top_max; k < bottom_max+1; k++) {
		left.push_back(make_pair(k, left_max));
	}

	for (int k = left_max; k < right_max+1; k++) {
		bottom.push_back(make_pair(bottom_max, k));
	}
	island.push_back(top);
	island.push_back(bottom);
	island.push_back(left);
	island.push_back(right);

	int min_x = -1;
	int min_y = -1;
	int min_bridge = 10;
	for (int k = 0; k < 4; k++) {
		for (int l = 0; l < island[k].size(); l++) {
			int len = 0;	
			int x = island[k][l].first;
			int y = island[k][l].second;
			int dxx = dx[k];
			int dyy = dy[k];
			while (0 <= x + dxx && x + dxx < n && 0 <= y + dyy && y + dyy < m) {
				if (maps[x + dxx][y + dyy] == 1 && visited[x+dxx][y+dyy] == false) {
					if (len < 2) break;
					else {
						cout << "len : " << len << endl;	
						//visited[x+dxx][y+dyy] = true;
						if (len < min_bridge){
							min_bridge = len;
							int min_x = x + dxx;
							int min_y = y + dyy;
							cout << "min_bridge : " << min_bridge << endl;
							cout << "min_x : " << min_x << endl;
							cout << "min_y : " << min_y << endl; 
						}
						//findBridge(x + dxx, y + dyy);
					}
				}
				
				if (maps[x+dxx][y+dyy] == 0) {
					len++;
				}
				x += dxx;
				y += dyy;
			}
		}
	}

	if (min_x != -1 && min_y != -1 && min_bridge != 10) {
		bridge_len += min_bridge;
		findBridge(min_x, min_y);
	}
};
int main() {
	cin >> n >> m;
	int tmp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j< m; j++) {
			cin >> tmp;
			maps[i][j] = tmp;
		}
	}
	bool res = true; 
	for (int i = 0; i < n; i++) {
		
		for (int j = 0; j < m; j++) {
			if (maps[i][j] == 1) {
				int a = i;
				int b = j;
				cout << "first : " <<  a << " " <<  b << endl; 

				findBridge(a ,b);
					
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (maps[i][j] == 1 && visited[i][j] == false) {
				bridge_len = -1;
				break;
			}
		}
	}

	cout << bridge_len << endl;
}