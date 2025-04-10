#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {0, 1, 1, 1, 0, 0, 0, -1, -1, -1};
int dy[] = {0, -1, 0, 1, -1, 0, 1, -1, 0, 1};
int N;
vector<pii> v;
priority_queue<int, vector<int>, greater<int>> pq;

void solve() {
    sort(v.begin(), v.end());

    pq.push(v[0].second);

    for(int i = 1; i < N; i++) {
        pq.push(v[i].second);

        if(pq.top() <= v[i].first) {
            pq.pop();
        }
    }

    cout << pq.size();
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back(make_pair(a, b));
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
