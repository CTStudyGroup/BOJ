#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int n, w, L;        // 트럭 개수, 트럭 길이, 최대 하중
queue<int> waiting;
queue<pii> bridge;      // 무게, 시간

void solve() {
    int time = 0;
    int weight = 0;

    while(!waiting.empty() || !bridge.empty()) {
        time++;

        if(!bridge.empty() && time - bridge.front().second >= w) {
            weight -= bridge.front().first;
            bridge.pop();
        }

        if(!waiting.empty() && weight + waiting.front() <= L && bridge.size() < w) {
            int next = waiting.front();
            waiting.pop();
            bridge.push({next, time});
            weight += next;
        }
    }

    cout << time;
}

void input() {
    cin >> n >> w >> L;

    for(int i = 0; i < n; i++) {
        int a;
        cin >> a;
        waiting.push(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
