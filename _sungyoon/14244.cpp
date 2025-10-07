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

int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M, cnt;
int i;

void solve() {
    if(M == 2) {
        for(int i = 0; i <= N-2; i++) {
            cout << i << " " << i+1 << endl;
        }
    }
    else {
        cout << 0 << " " << 1 << endl;

        for(i = 1; i <= M-1; i++) {
            cnt++;
            cout << 1 << " " << i+1 << endl;
        }

        if(i-1 < N-1) {
            for(int j = i; j < N-1; j++) {
                cout << j << " " << j+1 << endl;
            }
        }
    }
}

void input() {
    cin >> N >> M;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

