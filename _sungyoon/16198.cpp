#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N;
int result;
vector<int> v;

void bt(int len, int sum) {
    if(len == 2) {
        result = max(result, sum);
        return;
    }

    for(int i = 1; i < len-1; i++) {
        int energy = v[i-1] * v[i+1];
        int rm = v[i];
        v.erase(v.begin()+i);
        bt(len-1, sum + energy);
        v.insert(v.begin()+i, rm);
    }
}

void solve() {
    bt(N, 0);

    cout << result;
}

void input() {
    cin >> N;

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
