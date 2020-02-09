#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;
string ans;
bool visited[1001] = {false,};

void taskCount(stack <int> stk, vector <vector <int>> targeting, vector <vector <int>> targeted) {
	while (stk.size() > 0) {
		int x = stk.top();
		//cout << "node : " << x << endl;
		for (int i = 0; i < targeting[x].size(); i++) {
			int y = targeting[x][i];
			//cout << "target : " << y << endl;
			bool res = true;
			if (visited[y] == false) {
				for (int j = 0; j < targeted[y].size(); j++) {
					if (visited[targeted[y][j]] == false) {
						res = false;
						//cout << "res is false" << endl;
					}
				}

				if (res == true) {
					visited[y] = true;
					//cout << y << "is next" << endl;
					cout << " " << y;
					stk.push(y);
					taskCount(stk, targeting, targeted);
				}
			}
		}
		stk.pop();
	}
}

int main() {

	for (int tc = 1; tc < 11; tc++) {
		string ans = "";
		int V, E;
		cin >> V >> E;
		for (int i = 0; i < V+1; i++) {
			visited[i] = false;
		}
		vector <vector <int>> targeting(V+1);
		vector <vector <int>> targeted(V+1);
		cout << targeting.size() << endl;
		int node1, node2;
		for (int i = 0; i < E; i++) {
			cin >> node1 >> node2;
			//cout << node1 << endl;
			//cout << node2 << endl;
			targeting[node1].push_back(node2);
			targeted[node2].push_back(node1);
		}

		
		cout << "#" << tc;
		for (int i = 1; i < V+1; i++) {
			if (visited[i] == false) {
				bool res = true;
				for (int j = 0; j < targeted[i].size(); j++) {
					if (visited[targeted[i][j]] == false) {
						res = false;
						break;
					}
				}

				if (res == true) {
					visited[i] = true;
					cout << " " << i;
					stack <int> stk;
					stk.push(i);
					taskCount(stk, targeting, targeted);
				}
			}
		}
		cout << endl;
	}

	return 0;
}