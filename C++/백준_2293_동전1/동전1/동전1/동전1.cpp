#include <iostream>
#include <vector>
using namespace std;
int n, k;
int coins[10000] = {0, };
int coin_operation(int coins[10000]){
	int coin_dp[10000];
	int coin_dp_check[10000];
	coin_dp_check[0] = 1;
	int t = 0;
	for (int j = 0; j < k; j++) {
		// �������� �ʴ� ������ ���
		if (coins[j] == 0) {
			coin_dp[j] = 0;
		} else { // �����ϴ� ������ ���
			
		}
	}

}

int main() {
	vector <int> coins_count;
	cin >> n >> k;
	int temp;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		coins[i] = temp;
		coins_count.push_back(temp);
	}




}