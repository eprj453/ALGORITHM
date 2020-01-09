#include <iostream>
#include <cmath>
#include <queue>
#include <vector>
#include "pch.h"
using namespace std;
double maps[100][100];
int n, l, r;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

bool is_move(double present_state, double move_state) {
	double a, b;
	if (present_state >= move_state) {
		a = present_state;
		b = move_state;
	}
	else {
		a = move_state;
		b = present_state;
	}

	if (l <= a - b && a - b <= r) {
		return true;
	}
	else {
		return false;
	}
}
int move() {
	//double union_count = 0, union_population = 0;
	bool visited[100][100] = {false,};
	bool result = false;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			//bool can_move = false;
			if (visited[i][j] == false) {
				vector < pair <int, int> > country_list;
				double union_population = maps[i][j], union_count = 1;
				queue <pair <int, int>> q;
				q.push(make_pair(i, j));
				visited[i][j] = true;
				country_list.push_back(make_pair(i, j));
				while (q.size() > 0) {
					int x = q.front().first;
					int y = q.front().second;
					for (int k = 0; k < 4; k++) {
						if (0 <= x + dx[k] && x + dx[k] < n && 0 <= y + dy[k] && y + dy[k] < n) {
							if (visited[x + dx[k]][y + dy[k]] == false && is_move(maps[x][y], maps[x+dx[k]][y+dy[k]])) {
								q.push(make_pair(x + dx[k], y + dy[k]));
								country_list.push_back(make_pair(x + dx[k], y + dy[k]));
								visited[x + dx[k]][y + dy[k]] = true;
								union_population += maps[x + dx[k]][y + dy[k]];
							}
						}
					}
					q.pop();
				}


				if (country_list.size() > 1) {
					result = true;
					for (int t = 0; t < country_list.size(); t++) {
						int x = country_list[t].first;
						int y = country_list[t].second;
						maps[x][y] = floor(union_population / country_list.size());
					}
				}
					
			}
		}
	}

	return result;
}

int main() {
	double population;
	int answer = 0;
	cin >> n >> l >> r;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> population;
			maps[i][j] = population;
		}
	}

	while (move()) {
		answer++;
	}

	cout << answer << endl;
}