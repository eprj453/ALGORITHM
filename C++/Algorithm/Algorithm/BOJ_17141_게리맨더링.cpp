#include <iostream>
#include <stack>
#include <vector>
using namespace std;
int n;
int ans = 1000;
bool connect[10][10] = {false,};
bool visited[10];
int population[10] = {};
vector <int> set;
int dfsSize;

int min(int x, int y) {
	return x > y ? y : x;
}

bool DFS(bool check[10], stack <int> subset, bool visited[10]) {
	int subsetSize = subset.size();
	while (subset.size() > 0) {
		int x = subset.top();
		visited[x] = true;
		for (int k = 0; k < n ; k++) {
			if (x != k && connect[x][k] == true && check[k] == true && visited[k] == false) {
				visited[k] = true;
				subset.push(k);
				dfsSize++;
				DFS(check, subset, visited);
			}
		}

		subset.pop();
	}

	if (dfsSize == subsetSize) return true;
	else return false;
	
}

void findSubset() {
	for (int i = 0; i < (1 << n); i++) {
		stack <int> Aset;
		int Ap = 0; 
		bool Avisit[10] = {false,};
		for (int j = 0; j < n; j++) {
			if (i & (1 << j)) {
				Aset.push(set[j]);
				Avisit[set[j]] = true;
				Ap += population[set[j]];
			}
		}
		if (0 < Aset.size() && Aset.size() < n) {
			bool visited[10] = {false,};
			dfsSize = 1;
			bool Aresult = DFS(Avisit, Aset, visited);
			if (Aresult) {
				int Bp = 0;
				bool visited[10] = {false,};
				stack <int> Bset;
				bool Bvisit[10] = {false,};
				for (int k = 0; k < n; k++) {
					if (Avisit[k] == false) {
						Bset.push(set[k]);
						Bvisit[set[k]] = true;
						Bp += population[set[k]];
					}
				}
				dfsSize = 1;
				bool Bresult = DFS(Bvisit, Bset, visited);

				if (Aresult && Bresult) {
					ans = min(ans, abs(Ap - Bp));
				}
			}
		}
	}
}

int main(){
	int temp;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		population[i] = temp;
		set.push_back(i);
	}

	for (int i = 0; i < n; i++) {
		cin >> temp;
		int temp2;
		for (int j = 0; j < temp; j++) {
			cin >> temp2;
			connect[i][temp2-1] = true;
			connect[temp2-1][i] = true;
		}
	}

	findSubset();
	if (ans == 1000) cout << -1 << endl;
	else cout << ans << endl;
	return 0;
}

