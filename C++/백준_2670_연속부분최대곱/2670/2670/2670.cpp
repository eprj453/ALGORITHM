#include <iostream>
using namespace std;
double nums[10000];
int n;

double max_num (double x, double y) {
	return (x >= y) ? x : y;
}

double calculate() {
	double dp[10001];
	dp[0] = nums[0];
	double ans = nums[0];
	for (int k = 1; k < n; k++) {
		dp[k] = max_num(1, dp[k-1]) * nums[k];
		ans = max_num(ans, dp[k]);
	}

	return ans;
};

int main(){
	cin >> n;
	double t;

	for (int i = 0; i < n; i++) {
		cin >> t;
		nums[i] = t;
	}

	cout << fixed; 
	cout.precision(3);
	cout << calculate() << endl;

}