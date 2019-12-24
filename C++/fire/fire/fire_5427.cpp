#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

struct my_info {int x, y, d;};

queue<pair <int, int>> fires;
queue<pair <int, int>> me;

pair <int, int> start;

int find(queue<pair <int, int>> fires, queue<pair <int, int>> me) {
	int result = -1;

	return result;

}

void init() {
	while (!fires.empty()) {fires.pop();}
	while (!me.empty()) {me.pop();}
}

int main(){
	int dx[4] = {-1, 0, 1, 0};
	int dy[4] = {0, -1, 0, 1};

	int t;
	cin >> t;
	for (int tc = 1; tc < t+1; tc++) {
		int w, h;
		cin >> w >> h;
		vector < vector <int> > maps(w, vector <int> (h, 0));
		int min_distance = 1000000;
		int idx = 0;
		char temp;
		init();
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				
				cin >> temp;
				if (temp == '*') {
					fires.push(make_pair(i, j));
					maps[i][j] = 2;
				} 
				else if (temp == '@') {
					me.push(make_pair(i, j));
					maps[i][j] = 1;
				}
				else if (temp == '.') {
					maps[i][j] = 0;
				}
				else {maps[i][j] = -1;}
			}
		}
	}
}