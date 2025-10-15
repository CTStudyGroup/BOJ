#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
    int r;
};

int dx[] = {0, -1, 0, 1, 1, -1, -1, 1};
int dy[] = {-1, 0, 1, 0, -1, 1, -1, 1};
int V, E, P;
vector<vector<pii>> v(5001);
int dist[5001];
vector<int> tmp;

void dijkstra(int x) {
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, x});        // 비용, 정점
    dist[x] = 0;

    while(!pq.empty()) {
        int Node = pq.top().second;
        int cost = pq.top().first;
        pq.pop();

        if(dist[Node] < cost) continue;

        for(auto it : v[Node]) {
            int NextNode = it.first;
            int NextCost = cost + it.second;

            if(dist[NextNode] > NextCost) {
                pq.push({NextCost, NextNode});
                dist[NextNode] = NextCost;
            }
        }
    }
}

void Init() {
    for(int i = 1; i <= V; i++) {
        dist[i] = MAX;
    }
}

void solve() {
    Init();

    dijkstra(1);

    int gunwoo = dist[P];
    int end = dist[V];

    Init();
    dijkstra(P);

    if(end == gunwoo + dist[V]) cout << "SAVE HIM";
    else cout << "GOOD BYE";
}

void input() {
    cin >> V >> E >> P;

    for(int i = 0; i < E; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back({b, c});
        v[b].push_back({a, c});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

