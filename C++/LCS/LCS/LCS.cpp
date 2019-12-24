#include <iostream>
#include <string>
#include <vector>

using namespace std;

int search(vector<vector<int>> compare, string dna1, string dna2) {
	int max_val = 0;
	for (int i = 0; i < dna1.length(); i++) {
		for (int j = 0; j < dna2.length(); j++) {
			if (i == 0 || j == 0) {
				compare[i][j] = 0;
			} else if (dna1[i] == dna2[j]) {
				compare[i][j] = compare[i-1][j-1] + 1;
				if (compare[i][j] > max_val) {
				max_val = compare[i][j];}
			} else if (dna1[i] != dna2[j]) {
				compare[i][j] = max(compare[i-1][j], compare[i][j-1]);
			}

		}
	}


	return max_val;
}

int main(){
	int t;
	cin >> t;
	for (int tc = 1; tc < t+1; tc++) {
		string dna1, dna2;
		cin >> dna1;
		dna1 = " "+dna1;
		cin >> dna2;
		dna2 = " "+dna2;
		int len_1 = dna1.length();
		int len_2 = dna2.length();
		vector < vector <int> > compare (len_1, vector <int> (len_2, 0));
		
		cout << "#";
		cout << tc;
		cout << " ";
		cout << search(compare, dna1, dna2) << endl;
	
	}
}