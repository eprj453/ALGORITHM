#include <iostream>
#include <queue>
using namespace std;
int min(int x, int y) {
	if (x > y) {return y;}
	else {return x;}
}
int main(){
	int tc, n, m;
	cin >> tc;
	for (int t = 1; t < tc+1; t++) {
		int parking[101] = {0,};
		int fare[100]; 
		int temp; 
		int weight[2002];
		int parking_num[101];
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> temp;
			fare[i] = temp;
		}

		for (int i = 0; i < m; i++) {
			cin >> temp;
			weight[i] = temp;
		}
		int ans = 0;
		bool can_park = true;
		int parked_count = 0;
		int next_park = 0;
		queue <int> waiting; 
		for (int i = 0; i < 2*m; i++) {
			cin >> temp;
			if (temp < 0) { // 나가는 차량일 경우
				cout << temp << " 나감" << endl;
				temp = temp * -1;
				next_park = min(parking_num[temp-1], next_park);
				ans += (fare[parking_num[temp-1]] * parking[parking_num[temp-1]]);
				cout << ans << endl;
				can_park = true;

			} else { // 들어오는 차량일 경우
				cout << temp << " 들어옴" << endl;
				if (can_park  == false) { // 여유공간이 없을 경우
					waiting.push(temp-1);
					//parking[can_park] = make_pair(can_park, temp);
				} else {
					if (waiting.size() > 0) {
						parking[next_park] = waiting.front();
						waiting.push(temp-1);
						waiting.pop();
					} else {
						parking[next_park] = temp-1;
						parking_num[temp-1] = next_park;
					}
					while (next_park < n) {
						if (parking[next_park] == 0) {break;}
						else {next_park++;}
					}
					parked_count++;
					if (parked_count == n) {can_park = false;}
					}
				}
			}
			cout << ans << endl;
		}
	}
