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
int N, M;
vector<int> v;
bool visited[9];
int arr[9];
set<int> st;

void bt(int idx, int cnt) {
    if(cnt == M) {
        for(int i = 0; i < M; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    int tmp = 0;
    for(int i = idx; i < N; i++) {
        if(!visited[i] && v[i] != tmp) {
            visited[i] = true;
            arr[cnt] = v[i];
            tmp = v[i];
            bt(i, cnt+1);
            visited[i] = false;
        }
    }
}

void solve() {
    sort(v.begin(), v.end());

    bt(0, 0);
}

void input() {
    cin >> N >> M;

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
