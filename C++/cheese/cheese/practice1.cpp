#include <iostream>
#include <typeinfo> 

using namespace std;

int main(){
	int visited[4][4];
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2 ; j++) {
			visited[i][j] = i * j;
		}	
	}

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4 ; j++) {
			cout << visited[i][j] << " ";
			cout << typeid(visited[i][j]).name();
		}	
		cout << endl;
	}

}