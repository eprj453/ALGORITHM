## 서로소 집합(Union Find)

- find(x) : x의 그룹 번호 찾기
- union(x, y) : x와 y가 속한 그룹을 하나로 묶어준다.
- 트리로 구성.

```
int Find(int x) {
	if (P[x] == x) {return x}
	// P[x] = Find(x)
	return Find(P[x])
}
```



### 문제점

- 깊이가 너무 깊어질 경우 한칸씩 계속 타고 올라간다(시간이 너무 오래 걸림)

- // P[x] = Find(x)를 통해 부모를 찾아가는 모든 과정이 기록됨.

```
int union(int x, int y) {
	int x = Find(x)
	int y = Find(y)
	if () {}
}
```

