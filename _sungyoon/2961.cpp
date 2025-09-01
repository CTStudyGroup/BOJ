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
int N;
vector<pii> v;
int answer = MAX;

void solve() {
    for(int i = 1; i < (1 << N); i++) {
        int sour = 1;
        int bitter = 0;
        for(int j = 0; j < N; j++) {
            if(i & (1 << j)) {
                sour *= v[j].first;
                bitter += v[j].second;
            }
        }
        answer = min(answer, abs(sour - bitter));
    }

    cout << answer;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

