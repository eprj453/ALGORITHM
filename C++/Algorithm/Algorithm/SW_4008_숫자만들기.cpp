#include <iostream>
using namespace std;

int max_ans = -100000000;
int min_ans = 100000000;

void init() {
	max_ans = -100000000;
	min_ans = 100000000;
}
void operate(int opes[4], int nums[12],int start, int n, int sum_ans, int sum_ope) {
	if (sum_ope == 0) {
		max_ans = max(max_ans, sum_ans);
		min_ans = min(min_ans, sum_ans);
		return;
	} 
	if (opes[0] > 0) {
		opes[0] -= 1;
		operate(opes, nums, start+1, n, sum_ans + nums[start], sum_ope-1);
		opes[0] += 1;
	}
	if (opes[1] > 0) {
		opes[1] -= 1;
		operate(opes, nums, start+1, n, sum_ans - nums[start], sum_ope-1);
		opes[1] += 1;
	}
	if (opes[2] > 0) {
		opes[2] -= 1;
		operate(opes, nums, start+1, n, sum_ans * nums[start], sum_ope-1);
		opes[2] += 1;
	}
	if (opes[3] > 0) {
		opes[3] -= 1;
		operate(opes, nums, start+1, n, sum_ans / nums[start], sum_ope-1);
		opes[3] += 1;
	}
}
int main() {
	int t;
	cin >> t;
	for (int tc = 1; tc < t+1; tc++) {
		init();
		int n;
		cin >> n;
		int opes[4] = {0,};
		int sum_ope = 0;
		int nums[12];
		for (int i = 0; i < 4; i++) {
			int ope;
			cin >> ope;
			opes[i] = ope;
			sum_ope += ope;
		}

		for (int j = 0; j < n; j++) {
			int temp;
			cin  >> temp;
			nums[j] = temp;
		}
		operate(opes, nums, 1, n, nums[0], sum_ope);
		cout << "#" << tc << " " << max_ans - min_ans << endl;
	}
}