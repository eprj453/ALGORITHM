#include<iostream>

using namespace std;


int main(){
	int n, m, r, c, d;
	int dx[4] = {-1, 0, 1, 0};
	int dy[4] = {0, 1, 0, -1};
	
	cin >> n >> m;
	cin >> r >> c >> d;

    bool visited[50][50] = {false,}
    int maps[50][50];
    
    int temp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> temp;
			maps[i][j] = temp;
		}
	}

	visited[r][c] = true;
	int clean_count = 1;

	while (true) {
		bool can_spin = false;
		for (int i = 0; i < 4; i++) {
			int left = (d - i + 3) % 4;
			if (visited[r+dx[left]][c+dy[left]] == false && maps[r+dx[left]][c+dy[left]] == 0) {
				visited[r+dx[left]][c+dy[left]] = true;
				r = r+dx[left];
				c = c+dy[left];
				d = left;
				can_spin = true;
				++clean_count;
				break;
			}
		}

		bool can_back = false;
		if (can_spin == false) {
			int back = (d+2)%4;
			if (maps[r+dx[back]][c+dy[back]] == 0) {
				can_back = true;
				visited[r+dx[back]][c+dy[back]] = true;
				r = r+dx[back];
				c = c+dy[back];
			}
		}

		if (can_spin == false && can_back == false) {
			break;
		}
	}
	cout << clean_count << endl;
	return 0;
}