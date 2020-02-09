#include <iostream>
#include <vector>
using namespace std;

int n;
int maps[10][10];
int b_count = 0;
int w_count = 0;
int dx[4] = {1, -1, 1, -1};
int dy[4] = {1, 1, -1, -1};
void DFS(int start, vector <pair <int, int>> bishops, int count, int visited[10][10], char color) {

	if (start >= bishops.size()) {
		if (color == 'b') {
			b_count = max(b_count, count);
		} else if (color == 'w') {
			w_count = max(w_count, count);
		}
		return;
	}
	
	int x = bishops[start].first;
	int y = bishops[start].second;

	bool res = true;

	for (int k = 0; k < 4; k++) {
		int xk = x + dx[k];
		int yk = y + dy[k];
		if (res == false)  break;
		if (0 <= xk && xk < n && 0 <= yk && yk < n) {
			while (0 <= xk && xk < n && 0 <= yk && yk < n) {
				if (maps[xk][yk] == 1 && visited[xk][yk] == true) {
					res = false;
					break;
				}
				xk += dx[k];
				yk += dy[k];
			}
		}
	}

	if (res == false) {
		DFS(start + 1, bishops, count, visited, color);
	} else {
		visited[x][y] = true;
		DFS(start + 1, bishops, count+1, visited, color);
		visited[x][y] = false;
		DFS(start + 1, bishops, count, visited, color);
	}
}

int main() {
	vector <pair <int, int>> b_bishops;
	vector <pair <int, int>> w_bishops;
	cin >> n;
	int temp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> temp;
			maps[i][j] = temp;
			if (temp == 1) {
				if ((i + j) % 2 == 0) {
					b_bishops.push_back(make_pair(i, j));
				} else {
					w_bishops.push_back(make_pair(i, j));
				}
			}
		}
	}
	int visited[10][10] = {0,};

	DFS(0, b_bishops, 0, visited, 'b');
	DFS(0, w_bishops, 0, visited, 'w'); 
	cout << b_count + w_count << endl;
	

	return 0;
}