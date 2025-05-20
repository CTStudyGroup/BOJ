#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    int y;
};

int dx[] = {-1 ,1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, K, res;
int arr[9];
bool visited[9];
int result[9];

bool isvalid() {
    int muscle = 500;

    for(int i = 0; i < N; i++) {
        muscle += result[i];
        if(muscle < 500) {
            return false;
        }
    }
    return true;
}

void bt(int idx, int cnt) {
    if(cnt == N) {
        if(isvalid()) {
            res++;
        }
        return;
    }

    for(int i = 0; i < N; i++) {
        if(!visited[i]) {
            visited[i] = true;
            result[idx] = arr[i];
            bt(idx+1, cnt+1);
            visited[i] = false;
        }
    }
}

void solve() {
    bt(0, 0);

    cout << res;
}

void input() {
    cin >> N >> K;

    for(int i = 0;  i < N; i++) {
        cin >> arr[i];
        arr[i] -= K;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
