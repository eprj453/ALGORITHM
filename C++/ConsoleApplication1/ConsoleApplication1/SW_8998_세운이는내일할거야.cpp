// ConsoleApplication1.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include "pch.h"
#include <iostream>
using namespace std;

int min(int x, int y) {
	return x < y ? x : y;
}
struct task {
	int num;
	int start;
	int end;
}Task;
int testcase;
int main()
{
	cin >> testcase;
	for (int tc = 1; tc < testcase + 1; tc++) {
		int n, t, d;
		int ans = 0;
		int task_num[1000000000] = {0,};
		task tasks[1000000];
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> t >> d;

		}
	}
}
