#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    char map[5][7];
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N;
vector<pii> v;
int result;

void solve() {
    sort(v.begin(), v.end());

    priority_queue<int, vector<int>, greater<int>> pq;

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
