#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, K;
int arr[10001];
vector<int> v;
vector<int> res;

void solve() {
    sort(v.begin(), v.end());

    for(int i = 1; i < N; i++) {
        int tmp = v[i] - v[i-1];
        res.push_back(tmp);
    }

    sort(res.begin(), res.end());

    int result = 0;
    for(int i = 0; i < N-1 - (K-1); i++) {
        result += res[i];
    }

    cout << result;
}

void input() {
    cin >> N >> K;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        v.push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
