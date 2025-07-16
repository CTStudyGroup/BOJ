#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0,1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, M, K;
vector<pii> v;

struct cmp {
    bool operator()(pii a, pii b) {
        if(a.first == b.first) return a.second < b.second;
        return a.first > b.first;
    }
};

bool compare(pii a, pii b) {
    if(a.second == b.second) return a.first > b.first;
    return a.second < b.second;
}

void solve() {
    sort(v.begin(), v.end(), compare);
    priority_queue<pii, vector<pii>, cmp> pq;

    int cnt = 0;
    int maxlevel = 0;
    for(auto it : v) {
        int prefer = it.first;
        int level = it.second;
        pq.push({prefer, level});
        cnt += prefer;

        if(pq.size() == N) {
            if(cnt < M) {       // 선호도가 충족이 되지 않은 경우
                int stand = pq.top().first;
                pq.pop();
                cnt -= stand;
            }
            else {
                while(!pq.empty()) {
                    int level = pq.top().second;
                    pq.pop();
                    maxlevel = max(level, maxlevel);
                }
                cout << maxlevel;
                return;
            }
        }
    }
    cout << -1;
}

void input() {
    cin >> N >> M >> K;

    for(int i = 0; i < K; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
