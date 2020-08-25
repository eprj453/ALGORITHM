# 최단 경로 (shortest path)

## 정쌤 코드(dijkstra)

```python
from queue import PriorityQueue

def DIJKSTRA_PRIORITYQ(s):

    D = [0xfffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        d, u = Q.get()
        if d > D[u]: continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put((D[v], v))

    print(D[1: V + 1])
    print(P[1: V + 1])


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

DIJKSTRA_PRIORITYQ(1)
```



## Single-source (One to All)

- 하나의 출발 노드 s로부터 다른 노드까지의 최단 경로
  - dijkstra의 알고리즘



## Single-destination

- 모든 노드로부터 하나의 목적지 노드까지의 최단 경로
- single-source 문제와 동일



## Single-pair(One to One)

- 주어진 하나의 출발 노드 s로부터 하나의 목적지 t까지의 최단 경로
- 최악의 경우 시간복잡도에서 Single-source 문제보다 나은 알고리즘이 없음



## All-pairs

- 모든 노드 쌍에 대해서 최단 경로를 찾아라.
- Floyd 알고리즘, 



알고리즘에 따라 음수 가중치가 있어도 작동하는 경우도 있고 그렇지 않은 경우도 있음.

음수 가중치...? 잘 없는거 같다.

음수 가중치와는 별개로, 음수 사이클이 존재하는 경우(한 사이클이 존재하고, 그 사이클의 가중치 합이 음수인 경우)에는 최단 경로가 성립할 수 없다 (돌면 돌수록 가중치가 음수가 되면서 길이가 더욱 짧아지게 되므로).





## 최단 경로의 어떤 부분경로도 역시 최단 경로이다.

greedy한 방식으로 생각해볼 수 있다.



## 최단 경로는 사이클을 포함하지 않는다.

- 음수 사이클이 없다는 가정 하에, 최단 경로는 사이클을 포함하지 않는다(바로 가면 된다)



## input, output

- Input : 음수 사이클이 없는 가중치 방향 그래프와 출발 노드 s
- 목적 : 각 노드 v에 대해 다음을 계산한다.
  - d[v] :  모두 무한대와 같은 큰 값을 두고 시작
    - d[s] : 0으로 두고 시작 (자기 자신까지의 거리는 0)
    - 알고리즘이 진행됨에 따라 d[v]를 감소시킨다. 그러나 여기에서 항상 d[v] >= δ(s, v)를 유지한다.
    - 최종적으로 d[v] = δ(s, v)가 된다.
  - π[v] : s에서 v까지의 최단경로상에서 v의 직전 노드 (실제 경로)



### Relax

```
RELAX(u, v, w):
	# 현재 node의 최단 경로가 연결되어 있는 node의 최단 경로 + 그 node와의 가중치보다 클 경우 갱신
	if d[v] > d[u] + w(u, v):
		d[v] = d[u] + w(u, v)
		π[v] = u
```





## Generic-Single-Source(G,w,s)

1. 가중치와 연결 모두 초기화 (가중치는 무한대로, 연결은 자기 자신으로)

2. 해당 node와 연결되어 있는 node간에 relax 수행

3. 변화가 없을때까지 2번 반복



### 이렇게 하면, 최단 경로가 찾아지는가? 찾아진다면 2번을 얼마나 반복해야 하는가?



어떠한 최단경로라도, edge의 갯수가 node 갯수-1개보다 많을 수 없다.



## bellman-ford 알고리즘

```python
for i in range(1, v): #1부터 n-1(node 갯수 -1)까지
	for v, w in G[]: # i와 연결되어 있는 node 검사
        if d[v] > d[u] + w(u, v): # relax
                d[v] = d[u] + w(u, v)
                π[v] = u
                
for i in range(1, v):
   	for v, w in G[i]:
        if d[v] > d[u] + w(u, v)
       		return false
        
```





## dijkstra 알고리즘

출발 노드의 distance를 0으로 하고 출발, 그러나 현재 Node와 연결된 Node 중 d[v]가 최소인 Node를 판별해 찾아가고, 한 번 방문했던 Node는 다시 방문하지 않는다. 여기서 최소 힙이나 우선순위 큐를 이용해 최소인 Node를 저장할 수 있다.





## floyd-warshall 알고리즘

모든 노드 쌍들간의 최단경로의 길이를 구함.

d^k[i, j]

- 중간의 노드집합 {1, 2, 3, ..... k}에 속한 노드들만 거쳐서 노드 i에서 j까지 도달하는 최단경로의 길이

동적계획법이다.



Node I와 Node J를 잇는 방법은 2가지가 있다.

- Node 집합 {1, 2, 3 .... k}에 속한 노드 k를 지나는 경우
- 노드 k를 지나지 않는 경우



### Node k를 지나지 않는 경우

- 중간 정점들이 모두 {1, 2, 3 .... k}에 속함
- d^k[i, j] = d^k-1[i, j]

### Node k를 지나는 경우

- i -> k && k -> j
- 2가지로 나눠 생각해 본다면,
- i -> k
  - d^k-1[i, k]
- k -> j
  - d^k-1[k, j]
- 이 둘의 합이 d^k[i, j]가 된다.



지나는 경우와 지나지 않는 경우 중 더 짧은 경우가 최단 경로가 된다.

```
floydWarshall(G):
    for i in range(1, n):
        for j in range(1, n):
            d[k][i][j] = w[i][j] if w[i][j] else inf
    for k in range(1, n):
    	for i in range(1, n):
    		for j in range(1, n):
    			d[k][i][j] = min(d[k-1][i][j], d[k-1][i][k] + d[k-1][k][j])
```

시간복잡도 O(n^3)

시간복잡도가 좀 쎄다.

여러 Node들의 경로를 봐야한다면 dijkstra를 여러 번 실행하는 것보다 이게 더 이득일 수 있다. Node i와 Node j가 Node k를 지나는 경우와 지나지 않는 경우를 판단해야 하므로 3차원 배열이 필요하다.



```
floydWarshall(G):
    for i in range(1, n):
        for j in range(1, n):
            d[i][j] = w[i][j] if w[i][j] else inf
    for k in range(1, n):
    	for i in range(1, n):
    		for j in range(1, n):
    			d[i][j] = min(d[i][j], d[i][k] + d[k][j])
```

이렇게 2차원 배열로 구현해도 문제없다.



```
floydWarshall(G):
	π = 2차원 배열 inf 초기화
    for i in range(1, n):
        for j in range(1, n):
            d[i][j] = w[i][j] if w[i][j] else inf
            
    for k in range(1, n):
    	for i in range(1, n):
    		for j in range(1, n):
    			if d[i][j] > d[i][k] + d[k][j]):
    				d[i][j] = d[i][k], d[k][j]
    				π[i][j] = k;
```



i에서 j까지 가는 최단경로는 i -> k에서 가는 최단경로 + k -> j로 가는 최단경로의 합!

