#include <iostream>
using namespace std;

double max_num (double x, double y) {
	if (x >= y) {
		return x;
	} else {
		return y;
	}
}

double calculate(int t, double nums[10000]) {
	double dp[10001];
	dp[0] = nums[0];
	double ans = nums[0];
	for (int k = 1; k < t; k++) {
		dp[k] = max_num(1, dp[k-1]) * nums[k];
		ans = max_num(ans, dp[k]);
	}

	return ans;
};

int main(){
	int n;
	cin >> n;
	double nums[10001], t;

	for (int i = 0; i < n; i++) {
		cin >> t;
		nums[i] = t;
	}

	cout << fixed; 
	cout.precision(3);
	cout << calculate(n, nums) << endl;

}