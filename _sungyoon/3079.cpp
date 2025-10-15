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

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {-2, -2, 0, 0, 2, 2};
int dy[] = {-1, 1, -2, 2, -1, 1};
int N, M;

void solve(vector<int> &v) {
    ll lo = 1;
    ll hi = 1e18;
    ll answer = MAX;

    while(lo <= hi) {
        ll mid = (lo + hi) / 2;

        ll people = 0;
        for(int i = 0; i < N; i++) {
            people += mid / v[i];

            if(people >= M) {
                break;
            }
        }

        if(people >= M) {
            answer = mid;
            hi = mid - 1;
        }
        else lo = mid + 1;
    }

    cout << answer;
}

void input() {
    cin >> N >> M;

    vector<int> v(N, 0);

    for(auto &it : v) {
        cin >> it;
    }

    solve(v);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

