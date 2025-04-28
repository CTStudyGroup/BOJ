#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0};
int dy[] = {0, 0, -1, 1};
int N, L;
vector<pii> v;

void solve() {
    sort(v.begin(), v.end());

    int len = 0;        // 널판지 좌표
    int cnt = 0;
    for(int i = 0; i < N; i++) {
        int s = v[i].first;
        int e = v[i].second;

        if(len >= v[i].second) continue;

        if(s < len) s = len;

        int res = (e - s) / L;
        if((e - s) % L != 0) res++;
        len = s + res * L;
        cnt += res;

//        if(len < v[i].first) {
//            int tmp = v[i].second - v[i].first % L;
//            if(tmp > 0) {
//                cnt += (v[i].second - v[i].first / L) + 1;      // 발판 개수
//
//            }
//        }
    }

    cout << cnt;
}

void input() {
    cin >> N >> L;

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
