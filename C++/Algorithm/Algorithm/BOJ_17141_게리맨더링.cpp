#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int ans = 1000;
bool connect[10][10] = {false,};
int population[10];

int min(int x, int y) {
	return x > y ? y : x;
}

void findConnect(int n, queue <int> Aside, queue <int> Bside, bool Acheck[10], bool Bcheck[10]) {
	int Asize = Aside.size();
	int Bsize = Bside.size();
	
	int Apopulation = 0;
	int Bpopulation = 0;
	bool visited[10] = {false,};

	queue <int> Aq;
	queue <int> Bq;
	Aq.push(Aside.front());
	Bq.push(Bside.front());

	int Atemp = Aq.size(), Btemp = Bq.size();

	visited[Aq.front()] = true;
	while (Aq.size() > 0) {
		int x = Aq.front();
		//Atemp++;
		//visited[x] = true;
		for (int k = 0; k < n; k++ ) {
			if (connect[x][k] == true && Acheck[k] == true && visited[k] == false) {
				visited[k] = true;
				Aq.push(k);
				Atemp++;
			}
		}
		Aq.pop();
	}

	if (Asize == Atemp) {
		visited[Bq.front()] = true;
		while (Bq.size() > 0) {
			int x = Bq.front();
			//Btemp++;
			for (int k = 0; k < n; k++) {
				if (connect[x][k] == true && Bcheck[k] == true && visited[k] == false) {
					visited[k] = true;
					Bq.push(k);
					Btemp++;
				}
			}
			Bq.pop();
		}
	}

	if (Atemp == Asize && Btemp == Bsize) {
		while (Aside.size() > 0) {
			Apopulation += population[Aside.front()];
			Aside.pop();
		}
		while (Bside.size() > 0) {
			Bpopulation += population[Bside.front()];
			Bside.pop();
		}
		ans = min(ans, abs(Bpopulation - Apopulation));
	}

	return;
}

void findSubset(int n, int location[10]) {
	for (int i = 0; i < (1 << n); i++) {
		//vector <int> Aside;
		queue <int> Aside;
		bool Acheck[10] = {false,};
		for (int j = 0; j < n; j++) {
			if (i & (1 << j)) {
				Aside.push(j);
				Acheck[j] = true;

			}
		}
		
		int Asize = Aside.size();
		if (0 < Asize && Asize < n) {
			queue <int> Bside;
			bool Bcheck[10] = {false,};
			for (int k = 0; k < n; k++) {
				if (Acheck[k] == false) {
					Bside.push(k);
					Bcheck[k] = true;
				}
			}
			findConnect(n, Aside, Bside, Acheck, Bcheck);
		}
	}
}

int main() {
	int	n;
	int location[10];
	int temp;

	cin >> n;
	for (int i = 0; i < n+1; i++) {
		if (i == 0) {
			for (int j = 0; j < n; j++) {
				cin >> temp; 
				population[j] = temp;
				location[j] = j;
			} 
		} else {
			cin >> temp;
			int temp2;
			for (int j = 0; j < temp; j++) {
				cin >> temp2;
				connect[temp2][i-1] = true;
				connect[i-1][temp2] = true;
			}
		}
	}

	findSubset(n, location);
	if (ans == 1000) {
		cout << -1 << endl;
	} else {
		cout << ans << endl;
	}
}