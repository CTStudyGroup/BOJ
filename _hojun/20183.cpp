#include <bits/stdc++.h>
#define INF 1e15

typedef long long ll;
using namespace std;

vector<vector<pair<ll, ll>>> graph;
vector<ll> Distance;
ll n, m, a, b, cost;
ll max_w = 0; 

void Dijkstra(ll X) {
    priority_queue<pair<ll, ll>> pq;
    Distance[a] = 0;
    pq.push(make_pair(0, a));

    while (!pq.empty()) {
        ll CurC = -pq.top().first;
        ll CurX = pq.top().second;
        pq.pop();

        if (Distance[CurX] < CurC) {
            continue;
        }

        for (int i = 0; i < graph[CurX].size(); i++) {
            ll nextC = graph[CurX][i].second;

            if (nextC > X) {
                continue;
            }

            ll nextX = graph[CurX][i].first;

            if (Distance[nextX] > CurC + nextC) {
                if (CurC + nextC <= cost) {
                    Distance[nextX] = CurC + nextC;
                    pq.push(make_pair(-Distance[nextX], nextX));
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);

    cin >> n >> m >> a >> b >> cost;
    graph.resize(n + 1);

    for (ll i = 0; i < m; i++) {
        ll U, V, W;
        cin >> U >> V >> W;
        graph[U].push_back(make_pair(V, W));
        graph[V].push_back(make_pair(U, W));
        max_w = max(max_w, W); 
    }

    ll answer = INF;
    ll left = 0;
    ll right = max_w; 

    while (left <= right) {
        ll MID = (left + right) / 2;

        Distance.assign(n + 1, INF);

        Dijkstra(MID);
        if (Distance[b] != INF) {
            answer = MID;
            right = MID - 1;
        }
        else {
            left = MID + 1;
        }
    }

    if (answer == INF) {
        cout << -1 << "\n";
    }
    else {
        cout << answer << "\n";
    }

    return 0;
}