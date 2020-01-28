#include <iostream>
#include <stack>
using namespace std;

int * parent;
int parents;
int crossNode;


void upstream(int node, int parents[10001], bool visit1[10001]) {
	int tmp = node;
	int x = 0;
	while (x < 10001) {
		if (visit1[tmp] == true) {
			crossNode = tmp;
			return;
		} else {
			if (!parents[tmp]) {
				visit1[tmp] = true;
				return;
			}
			else {
				visit1[tmp] = true;
				tmp = parents[tmp];
			}
		}
		x++;
	}
	//return 0;
}

int main() {
	int t, v, e, ans1, ans2;
	int prt, chd;
	
	cin >> t;
	
	for (int tc = 1; tc < t+1; tc++) {
		int children[10001][2] = {0,};
		int parents[10001] = {0,};
		cin >> v >> e >> ans1 >> ans2;
		for (int i = 0; i < e; i++) {
			cin >> prt >> chd;
			parents[chd] = prt;
			if (children[prt][0]) {
				children[prt][1] = chd;
			} else children[prt][0] = chd;
		}

		bool visit1[10001] = {false,};
		bool visit2[10001] = {false,};
		
		crossNode = 0;
		upstream(ans1, parents, visit1);
		upstream(ans2, parents, visit1);
		//cout << crossNode << endl;
		int childrenSize = 0;
		if (crossNode != 0) {
			stack <int> st;
			visit2[crossNode] = true;
			st.push(crossNode);
			while (st.size() > 0) {
				int x = st.top();
				bool chk = false;
				for (int k = 0; k < 2; k++) {
					if (visit2[children[x][k]] == false) {
						st.push(children[x][k]);
						childrenSize++;
						visit2[children[x][k]] = true;
						chk = true;
						break;
					}
				}

				if (!chk) st.pop();

			}
		}
		cout << "#" << tc << " " << crossNode << " " << childrenSize << endl;
	}


}