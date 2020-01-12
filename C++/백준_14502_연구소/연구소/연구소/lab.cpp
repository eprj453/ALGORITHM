#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int ans = 0;
vector <pair<int, int>> temp;
int n, m;
int r = 3;
int min_virus;
int max_safe;
vector <pair <int, int>> viruses;
vector <pair<int, int>> safe_zones;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void init(){
	safe_zones.clear();
	temp.clear();
	viruses.clear();
	min_virus = 64;
}

void spread_virus(char maps[8][8]) {
	//cout << "call" << endl;
	//vector < vector <bool> > v_visited;

	bool v_visited[8][8];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			v_visited[i][j] = false;
		}
	}

	// 벽을 세운다.
	for (int i = 0; i < 3; i++) {
		maps[temp[i].first][temp[i].second] = '1';
	}

	int virus_count = 0;
	queue <pair <int, int> > q;

	int t = 0;
	//cout << viruses.size() << endl;
	while (t < viruses.size()) {
		q.push(viruses[t]);
		v_visited[viruses[t].first][viruses[t].second] = true;
		t++;
		//virus_count++;
	}

	while (q.size() > 0) {
		int x = q.front().first;
		int y = q.front().second;
		for (int k = 0; k < 4; k++) {
			if (0 <= x + dx[k] && x + dx[k] < n && 0 <= y + dy[k] && y + dy[k] < m) {
				if (maps[x+dx[k]][y+dy[k]] == '0' && v_visited[x+dx[k]][y+dy[k]] == false) {
					v_visited[x+dx[k]][y+dy[k]] = true;
					virus_count++;
					q.push(make_pair(x + dx[k], y+dy[k]));
					if (virus_count > min_virus) {

						break;
					}
				}
			}
		}
		q.pop();
	}

	//cout << "virus_count : " << virus_count << endl;
	if (min_virus >= virus_count && virus_count != -1){
		min_virus = virus_count;
	}
	// 다시 벽 해제
	for (int i = 0; i < 3; i++) {
		maps[temp[i].first][temp[i].second] = '0';
	}

	return;
}

void comb(int k, int start, vector <pair<int, int>> safe_zones, char maps[8][8]) {
	//cout << "ccomb call" << endl;
	if (k == r) {
		//cout << "spread call" << endl;
		spread_virus(maps);
		return;
	} else {
		for (int i = start; i < safe_zones.size(); i++) {
			temp.push_back(safe_zones[i]);
			comb(k+1, i+1, safe_zones, maps);
			temp.pop_back();
		}
	}
}

int main(){
	cin >> n >> m;
	init();
	char maps[8][8];
	char temp;
	int init_virus = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> temp;
			if (temp == '0') {
				safe_zones.push_back(make_pair(i, j));
			} else if (temp == '2') {
				viruses.push_back(make_pair(i, j));
				init_virus++;
			}
			maps[i][j] = temp;
		}
	}
	
	comb(0, 0, safe_zones, maps);
	//cout << "min_count : " << min_count << endl;
	//cout << "safe_zone : " << safe_zones.size() << endl;
	//cout << "min_virus : " << min_virus << endl;
	cout << safe_zones.size() - min_virus - 3 << endl;

	return 0;
}