#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};
pair <int, int> cctvs[8];
int n, m;
int ans = 64;
int cctvCount = 0;


void search(int cnt, int maps[8][8], int invisibleCount) {
	
	if (cnt == cctvCount) {
		if (invisibleCount < ans) { 
			ans = invisibleCount; 
		}
		return;
	}
	
	int x = cctvs[cnt].first;
	int y = cctvs[cnt].second;
	if (maps[x][y] == 1) {
		for (int k = 0; k < 4; k++) {
			int tempCount = 0;
			int xx = dx[k];
			int yy = dy[k];
			int copyMaps[8][8];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					copyMaps[i][j] = maps[i][j];
				}
			}
			while (0 <= x + xx && x + xx < n && 0 <= y + yy && y + yy < m && copyMaps[x + xx][y + yy] != 6) {
				if (copyMaps[x + xx][y + yy] == 0) {
					copyMaps[x + xx][y + yy] = 7;
					tempCount++;
				}
				
				xx += dx[k];
				yy += dy[k];
				
			}
			search(cnt + 1, copyMaps, invisibleCount - tempCount);
		}
	}
	if (maps[x][y] == 2) {
		for (int k = 0; k < 2; k++) {
			int tempCount = 0;
			int copyMaps[8][8];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					copyMaps[i][j] = maps[i][j];
				}
			}
			for (int l = k; l < 4; l+=2) {
				int xx = dx[l];
				int yy = dy[l];
				while (0 <= x + xx && x + xx < n && 0 <= y + yy && y + yy < m && copyMaps[x + xx][y + yy] != 6) {
					if (copyMaps[x + xx][y + yy] == 0) {
						copyMaps[x + xx][y + yy] = 7;
						tempCount++;
					}
					xx += dx[l];
					yy += dy[l];
				}
			}
			search(cnt + 1, copyMaps, invisibleCount - tempCount);
		}
	}
	if (maps[x][y] == 3) {
		for (int k = 0; k < 4; k++) {
			int tempCount = 0;
			int copyMaps[8][8];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					copyMaps[i][j] = maps[i][j];
				}
			}
			for (int l = k; l < k+2; l++) {
				int xx = dx[l%4];
				int yy = dy[l%4];
				
				while (0 <= x + xx && x + xx < n && 0 <= y + yy && y + yy < m && copyMaps[x + xx][y + yy] != 6) {
					if (copyMaps[x + xx][y + yy] == 0) {
						copyMaps[x + xx][y + yy] = 7;
						tempCount++;
					}
					xx += dx[l%4];
					yy += dy[l%4];
				}
			}
			search(cnt + 1, copyMaps, invisibleCount - tempCount);
		}
	}
	if (maps[x][y] == 4) {
		for (int k = 0; k < 4; k++) {
			int tempCount = 0;
			int copyMaps[8][8];
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					copyMaps[i][j] = maps[i][j];
				}
			}
			for (int l = k; l < k + 3; l++) {
				int xx = dx[l % 4];
				int yy = dy[l % 4];
				
				while (0 <= x + xx && x + xx < n && 0 <= y + yy && y + yy < m && copyMaps[x + xx][y + yy] != 6) {
					if (copyMaps[x + xx][y + yy] == 0) {
						copyMaps[x + xx][y + yy] = 7;
						tempCount++;
					}
					xx += dx[l%4];
					yy += dy[l%4];
				}
			}
			search(cnt + 1, copyMaps, invisibleCount - tempCount);
		}
	}
	if (maps[x][y] == 5) {
		int tempCount = 0;
		int copyMaps[8][8];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				copyMaps[i][j] = maps[i][j];
			}
		}
		for (int k = 0; k < 4; k++) {
			int xx = dx[k];
			int yy = dy[k];
			
			while (0 <= x + xx && x + xx < n && 0 <= y + yy && y + yy < m && copyMaps[x + xx][y + yy] != 6) {
				if (copyMaps[x + xx][y + yy] == 0) {
					copyMaps[x + xx][y + yy] = 7;
					tempCount++;
				}
				xx += dx[k];
				yy += dy[k];
			}
		}
		search(cnt + 1, copyMaps, invisibleCount - tempCount);
	}
}
	

int main() {
	//pair <int, int> cctvs[8];
	int maps[8][8];
	int temp;
	int invisibleZone = 0;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> temp;
			if (temp == 0) {
				invisibleZone++;
			}
			else {
				if (temp != 6) {
					cctvs[cctvCount++] = make_pair(i, j);
				}
			}
			maps[i][j] = temp;
		}
	}
	//invisibleZone;
	search(0, maps, invisibleZone);
	cout << ans << endl;
}