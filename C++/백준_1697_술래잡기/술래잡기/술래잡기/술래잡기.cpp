#include <iostream>
#include <queue>
using namespace std;

int main(){
	int n, k;
	cin >> n >> k;
	queue <pair <int, int>> q;
	q.push(make_pair(n, 0));
	bool visited[100001] = {false,};
	visited[n] = true;
	while (q.size() > 0) {
		int location = q.front().first;
		int count = q.front().second;
		if (location == k) {
			cout << count << endl;
			break;
		}
		
		if (location + 1 == k || location - 1 == k || location * 2 == k) {
			cout << count + 1 << endl;
			break;
		} else {
			if (location + 1 <= 100000 && visited[location+1] == false) {
				q.push(make_pair(location+1, count+1));
				visited[location+1] = true;
			} 
			
			if (location - 1 >= 0 && visited[location-1] == false) {
				q.push(make_pair(location-1, count+1));
				visited[location-1] = true;
			} 
			
			if (location * 2 <= 100000 && visited[location*2] == false) {
				q.push(make_pair(location*2, count+1));
				visited[location*2] = true;
			}
		}
		q.pop();
	}
	return 0;
}