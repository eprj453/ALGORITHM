#include <iostream>
#include <vector>
#include <stack>
using namespace std;
int connect = 0;
int visited[200] = {false,};
void dfs(int n, vector <vector <int>> computer) {
	for (int i = 0; i < n; i++) {
		if (visited[i] == false) {
			stack <int> stk;
			stk.push(i);
			visited[i] = true;
			while (stk.size() > 0) {
				int x = stk.top();
				for (int k = 0; k < n; k++) {
					if (x != k && computer[x][k] == true && visited[k] == true) {
						stk.push(k);
						visited[k] = true;
					}
				}
				stk.pop();
			}
		}
		connect++;
	}
}


int main() {
	
}