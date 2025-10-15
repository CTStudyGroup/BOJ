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
int G;
int arr[100001];
vector<int> v;

void solve() {
    int le = 1;
    int ri = 2;

    while(ri < 100001) {
        ll stand = (arr[ri] * arr[ri]) - (arr[le] * arr[le]);

        if(stand == G) {
            v.push_back(ri);
        }

        if(stand >= G) {
            le++;
        }
        else ri++;
    }

    if(v.empty()) {
        cout << -1;
        return;
    }

    for(auto it : v) {
        cout << it << " ";
    }
}

void Init() {
    for(int i = 1; i <= 100000; i++) {
        arr[i] = i;
    }
}

void input() {
    cin >> G;

    Init();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

