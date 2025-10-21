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

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
int A[4001];
int B[4001];
int C[4001];
int D[4001];


void solve() {
    vector<ll> AB;
    vector<ll> CD;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
            ll tmp = A[i] + B[j];
            ll tmps = C[i] + D[j];
            AB.push_back(tmp);
            CD.push_back(tmps);
        }
    }

    ll cnt = 0;
    sort(AB.begin(), AB.end());
    sort(CD.begin(), CD.end());

    for(int i = 0; i < AB.size(); i++) {
        ll tmp = -AB[i];

        ll low = lower_bound(CD.begin(), CD.end(), tmp) - CD.begin();
        ll high = upper_bound(CD.begin(), CD.end(), tmp) - CD.begin();

        if(tmp == CD[low]) cnt += (high - low);
    }

    cout << cnt;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < 4; j++) {
            if(j == 0) {
                cin >> A[i];
            }
            else if(j == 1) cin >> B[i];
            else if(j == 2) cin >> C[i];
            else cin >> D[i];
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

