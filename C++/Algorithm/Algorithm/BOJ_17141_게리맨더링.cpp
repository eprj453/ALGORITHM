#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int n;
int ans = 1000;
bool connect[11][11] = {false,};
int population[11] = {};
vector <int> set;

int min(int x, int y) {
	return x > y ? y : x;
}

bool findConnect(bool Acheck[11], bool Bcheck[11], queue <int> Asubset, queue <int> Bsubset) {

	int Asize = Asubset.size() -1, Bsize = Bsubset.size()-1;
	//int Atemp = 1, Btemp = 1;
	bool Avisited[10] = {false,};
	bool Bvisited[10] = {false,};
	Avisited[Asubset.front()] = true;
	Bvisited[Bsubset.front()] = true;
	bool Aresult = true;
	bool Bresult = true;
	while (Asubset.size() > 0) {
		int x = Asubset.front();
		bool t = false;
		for (int k = 0; k < n; k++) {
			if (x != k && connect[x][k] == true  && Acheck[k] == true && Bcheck[k] == false && Avisited[k] == false) {
				//Asubset.push(k);
				Asize--;
				Avisited[k] = true;

			};
		}
		Asubset.pop();
	}

	if (Asize == 0) {
		while (Bsubset.size() > 0) {
			int x = Bsubset.front();
			for (int k = 0; k < n; k++) {
				if (x != k && connect[x][k] == true && Bcheck[k] == true && Acheck[k] == false && Bvisited[k] == false) {
				//	Bsubset.push(k);
					Bvisited[k]= true;
					Bsize--;
				} else Bresult = false;
			}
			Bsubset.pop();
		}
	}

	if (Asize == 0 && Bsize == 0) {
		cout << "true" << endl;
		return true;
	} else return false;
}

void findSubset() {
	for (int i = 0; i < (1 << n); i++) {
		queue <int> Aset;
		bool Avisit[10] = {false,};
		for (int j = 0; j < n; j++) {
			if (i & (1 << j)) {
				Aset.push(set[j]);
				Avisit[j] = true;
			}
		}
		if (0 < Aset.size() && Aset.size() < n) {
			queue <int> Bset;
			bool Bvisit[10] = {false,};
			for (int k = 0; k < n; k++) {
				if (Avisit[k] == false) {
					Bset.push(set[k]);
					Bvisit[k] = true;
				}
			}
			
			if (findConnect(Avisit, Bvisit, Aset, Bset)) {
				int Ap = 0, Bp = 0;
				while (Aset.size() > 0) {
					Ap += population[Aset.front()];
					cout << Aset.front() << " ";
					Aset.pop();
				} cout << endl;

				while (Bset.size() > 0) {
					Bp += population[Bset.front()];
					cout << Bset.front() << " ";
					Bset.pop();
				} cout << endl;

				ans = min(ans, abs(Ap-Bp));
			}		
		}
	}
}

int main(){
	//int n;
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

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << connect[i][j] << " ";
		} cout << endl;
	}
	findSubset();
	cout << ans << endl;
	return 0;
}

6
2 2 2 2 2 2
1 3
1 4
1 1
1 2
1 6
1 5