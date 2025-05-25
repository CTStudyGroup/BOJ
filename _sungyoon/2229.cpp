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
int N;
int arr[1001];
int dp[1001];

void solve() {
    for(int i = 2; i <= N; i++) {
        // 혼자 있는 경우는 0이기 때문
        int minvalue = arr[i];
        int maxvalue = arr[i];
        for(int j = i-1; j >= 0; j--) {
            minvalue = min(arr[j+1], minvalue);
            maxvalue = max(arr[j+1], maxvalue);
            dp[i] = max(dp[i], dp[j] + maxvalue - minvalue);
        }
    }
    
    cout << dp[N];
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
