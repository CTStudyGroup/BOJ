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

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N, K;
int arr[1000002];
int result = MAX;

void solve() {
    int start = 0;
    int end = 0;
    int cnt = 0;
    if(arr[end] == 1) cnt++;

    while(end < N) {
        if(cnt == K) {
            result = min(end - start + 1, result);

            if(arr[start] == 1) cnt--;
            start++;
        }
        else {
            end++;
            if(arr[end] == 1) cnt++;
        }
    }

    if(result == MAX) cout << -1;
    else cout << result;
}

void input() {
    cin >> N >> K;

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
