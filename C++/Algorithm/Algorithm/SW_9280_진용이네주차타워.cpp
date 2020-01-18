#include <iostream>
#include <queue>
 
using namespace std;


int min(int x, int y) {
	if (x > y) {return y;}
	else {return x;}
}
int main(){
	//freopen("9280_input.txt", "r", stdin);
	int tc, n, m;
	cin >> tc;
	for (int t = 1; t < tc+1; t++) {
		int ans = 0;
		int parking[101] = {0,};
		int fare[100]; 
		int temp; 
		int weight[2001];
		int parking_num[2001];
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> temp;
			fare[i] = temp;
		}

		for (int i = 0; i < m; i++) {
			cin >> temp;
			weight[i] = temp;
		}
		bool can_park = true;
		int parked_count = 0;
		int next = 0;
		queue <int> waiting; 
		
		for (int i = 0; i < m*2; i++) {
			cin >> temp;
			if (temp > 0) {
				if (parked_count >= n) { // 빈자리가 없을 경우
					waiting.push(temp);
				} else { // 빈자리가 있을 경우
					if (waiting.size() > 0) { // 대기가 있을 경우
						int car = waiting.front();
						parking[next] = weight[car-1];
						cout << "들어가는 차 무게 : " << weight[car-1] << endl;
						parking_num[car] = next;
						cout << "들어가는 차 번호 : " << next << endl;
						next++;
						waiting.pop();
						waiting.push(temp);
					} else { // 대기도 없는 경우
						parking[next] = weight[temp-1];
						parking_num[temp] = next;
						cout << "들어가는 차 무게 : " << weight[temp-1] << endl;
						//parking_num[car] = next;
						cout << "들어가는 차 번호 : " << next << endl;
						next++;
					}

					while (next < n) {
						if (parking[next] == 0) break;
						else {next++;}
					}
					parked_count++;
				}
			} else { // 차가 나가는 경우
				temp = temp*-1;
				cout << "주차 위치 : " << parking_num[temp] << endl;
				ans += (fare[parking_num[temp]] * parking[parking_num[temp]]);
				cout << "요금 추가" << (fare[parking_num[temp]] * parking[parking_num[temp]]) << endl;
				next = min(next, parking_num[temp]);
				parking[parking_num[temp]] = 0;
				parked_count--;
				if (waiting.size() > 0) {
					int car = waiting.front();
					parking[next] = weight[car-1];
					cout << "들어가는 차 무게 : " << weight[car-1] << endl;
					parking_num[car] = next;
					cout << "들어가는 차 번호 : " << next << endl;
					waiting.pop();
				}

				while (next < n) {
					if (parking[next] == 0) {break;}
					else {next++;}
				}
			
			}
		}
		cout <<"#" << t<< " " << ans << endl;
	}
}


