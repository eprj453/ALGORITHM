# 최소 신장 트리(minimum spanning tree)

입력 : n개의 도시, 도시와 도시를 연결하는 비용

문제 : 최소 비용으로 모든 도시들이 서로 연결되게 하도록 하자.



무방향 가중치 그래프(가중치는 모두 양수라고 가정한다.)에서 최소 가중치의 합으로 모든 Node가 연결되도록 하는 Edge들의 부분집합!



MST가 유일하게 1개만 존재하는 것은 아니다(그래프의 모양은 여러개일 수 있다).



## 요약 

- 무방향 가중치 그래프 G = (V, E)
- 각 Edge (u ,v) 에 대한 가중치 W(u, v)
- 다음 조건을 만족하는 Edge들의 부분집합을 찾는 것!
  - 부분집합의 Edge들에 의해 모든 Node들이 서로 연결
  - 모든 가중치의 합이 최소





## 왜 Tree인가?

부모 - 자식 간의 계층적 구조를 갖는 자료구조를 Tree라고 하지만,

사이클이 없는 무방향 그래프도 Tree가 될 수 있다.

만약 사이클이 만들어진다면 Node의 중복연결이 이루어지므로 모든 가중치의 합이 최소라는 조건을충족하지 못한다.



## 많이 쓰인다.

공학 분야에서 (네트워크 연결, 도로 건설 등) 하나의 기준이 되어줄 수 있다.





# Generic MST 알고리즘

- 어떤 MST의 부분집합 A에 대해서 set(A) ∪ set((u, v))도 역시 어떠한 MST의 부분집합이라면, Edge (u, v)는 A에 대해서 안전하다고 한다.



1. 처음에는 공집합 A로 시작한다.
2. 집합 A에 대해서 안전한 Edge를 하나 찾은 후 이것을 A에 반복한다.
3. Edge의 갯수가 n-1개가 될 때까지 2번을 반복한다.



### 수도 코드

```
Generic MST(G, w):
	A = set()
	while A not Spanning tree:
		do find an edge(u, v) that is safe for A:
			A <- A U {(u, v)}
	return A
```





### 안전한 Edge 찾기

- 그래프의 정점들을 2개의 집합 S와 V-S로 분할한 것을 컷(cut), (S, V-S)라고 한다.
- Edge (u, v)에 대해서 u ∈ S이고 V ∈ V-S일때 (한 쪽은 집합1, 나머지 한 쪽은 다른 집합에 있을때) Edge는 컷(S, V-S)을 cross한다고 한다.

- Edge의 부분집합 A에 속한 어떤 Edge도 Cut(S, V-S)를 cross하지 않을 때, 컷 (S, V-S)은 A를 존중한다(respect)라고 한다.

![cut](https://user-images.githubusercontent.com/52685258/81220905-09bc2d00-901d-11ea-8406-72cfc20ae3d3.png)



lighest edge는 Edge의 집합 A에 대해 안전하다.

![unnamed](https://user-images.githubusercontent.com/52685258/81220906-0aed5a00-901d-11ea-918a-6e621299e83f.png)





## kruskal 알고리즘

- Edge들의 가중치를 오름차순으로 정렬한다.

- Edge들을 순서대로 하나씩 선택한다. 단, 이미 선택된 Edge들과 사이클을 형성할 경우 선택하지 않는다(Node들의 집합에 Edge 양 끝이 모두 포함되는 경우).

- n-1개의 Edge가 선택되면 종료한다.
- Edge의 가중치가 중복되더라도 어느 것을 먼저 선택해도 상관없다.







### kruskal이 어떻게 MST를 찾는가?

- 여태까지 알고리즘이 선택한 Edge의 집합 A가 있다고 한다면, cycle을 만들지 않는 최소 비용의 Edge를 포함하는 MST는 반드시 존재한다. 그렇기 때문에 kruskal 알고리즘에서 선택되는 최소 비용의 Edge는 항상 MST를 만드는 Edge이다.





### CYCLE을 만들지 않게 하는 방법

A~G의 Node가 있다고 한다면,

{A}, {B}, {C}, {D}, {E}, {F}, {G}

각각의 Node를 집합으로 표현한다.

그리고 Node가 이어질때마다 하나의 집합으로 묶어서 표현한다.

A, B 연결 -> {A, B}, {C}, {D},  {E},  {F},  {G}

이렇게 연결하면서 집합을 만들고, 연결하려는 두 Node가 같은 집합 안에 포함되어 있다면 연결 시 Cycle이 형성되므로 연결하지 않는다.



### 

### Node를 Tree로 연결하기

집합들은 서로 교집합을 갖지 않는다(disjoint set, 서로소).

Node가 갖는 집합을 찾을 때, 두 집합을 서로 합칠 때 이 구조가 필요하다.

이를 Union - find 라 한다.



각 집합을 하나의 Tree로 표현!

누가 root이고 누가 누구의 부모이든 상관이 없음(이진 트리나 그런거 아님)

트리의 각 Node는 자식 Node가 아닌 부모 Node의 주소를 갖는다 (root에서 밑으로 탐색하지 않고 밑에서 위로 탐색한다).



#### 부모가 누구인지를 저장하는 배열을 선언해, 부모를 찾자!



```python
def find_parent(node, parents):
    if parents[node] == node:
        return node
    root = find_parent(parents[node], parents)
    return root

parents = [x for x in range(Node 갯수+1)]

x, y = find_parent(first_node, parents), find_parent(second_node, parents)

if x != y:
    parents[x] = y # 부모 노드를 지정함으로써 같은 부모를 갖는 집합으로 묶어버림
```



위와 같은 방법은 한 번 union find를 할 때마다 시간 복잡도는 최대 O(n), 만약 자기 자신이 부모라면 O(1)의 복잡도를 갖게 된다.

부모 노드를 지정하는 것으로 같은 집합으로 묶는 과정은 무조건 O(1)의 복잡도를 갖는다.

find parent 2번이면 n짜리를 2번 하게 되므로 효율적으로 할 방법을 찾아보자.



1. **트리의 높이를 최대한 낮게 하자**

```python
size = [1 for _ in range(num+1)]
parents = [x for x in range(Node 갯수+1)]

x, y = find_parent(first_node, parents), find_parent(second_node, parents)

if x != y:
    if size[x] > size[y]: # node 갯수가 많은 쪽의 집합으로 종속시킨다
        parents[y] = x # x가 더 크므로 y의 부모를 -> x로
        size[x] += size[y] # x의 크기는 y만큼 증가
    else:
        parents[x] = y
        size[y] += size[x]
```



이 방법을 사용하면 무작정 합치는 것보다 효율적으로 n을 조절할 수 있다.



2. **Path compression ()**

```python
def find_parent(node, parents):
    while node != parents[node]:
        parents[node] = parents[parents[node]]
        node = parents[node]
    return parents[node]

parents = [x for x in range(Node 갯수+1)]

x, y = find_parent(first_node, parents), find_parent(second_node, parents)

if x != y:
    parents[x] = y
    bridge_num -= 1
    answer += w
```

![266D8650577C916C2D](https://user-images.githubusercontent.com/52685258/81503641-ae8d8180-931f-11ea-80b2-d5261fe70727.png)



위와 같이 경로를 최적으로 압축해 좋은 효율을 기대할 수 있다.





## Prim 알고리즘

1. 임의의 Node를 출발 Node로 선택
2. 출발 Node를 포함하는 Tree를 점점 키워감
3. 매 단계에서 [이미 Tree에 포함된 Node]와 포함되지 않은 Node를 연결하는 Edge들 중에 가장 Edge의 가중치가 작은 Edge를 선택





### Prim의 알고리즘에서 제일 중요한 것

- Tree에 포함된 Node, 그리고 그렇지 않은 Node를 어떻게 구분할것인가.
- 구분했다면, 연결하는 Edge 중에 가장 가중치가 작은 Edge는 어떻게 구분할 것인가?

최악의 경우 복잡도가 O(n^3)까지 갈 수 있음. 매우 비효율적이다.



### 그렇다면?

- 



 