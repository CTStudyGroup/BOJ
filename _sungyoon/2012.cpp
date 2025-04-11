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
vector<int> v1;
ll result;

void solve() {
    sort(v1.begin(), v1.end());

    for(int i = 1; i <= N; i++) {
        result += abs(v1[i-1] - i);
    }

    cout << abs(result);
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        v1.push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
