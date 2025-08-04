#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x;
    string s;
    vector<int> v;
};

int dx[] = {-1, 0, 1, 0, 1, -1, -1, 1};
int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
int T, N;
int arr[10001];
int tmp[10001];
priority_queue<int, vector<int>> pq;

void solve() {
    int idx = N / 2;
    int x = pq.top();
    pq.pop();
    int cnt = 1;
    tmp[idx] = x;

    while(!pq.empty()) {
        int maxval = pq.top();
        pq.pop();
        int minval = pq.top();
        pq.pop();

        tmp[idx+cnt] = maxval;
        tmp[idx-cnt] = minval;

        cnt++;

        if(pq.size() == 1) {
            int temp = pq.top();
            pq.pop();
            tmp[idx-cnt] = temp;
        }
    }

    int result = 0;

    for(int i = 1; i < N; i++) {
        result = max(result, abs(tmp[i] - tmp[i-1]));
    }
    result = max(result, abs(tmp[N-1] - tmp[0]));

    cout << result << endl;
}

void input() {
    cin >> T;

    while(T--) {
        cin >> N;

        for(int i = 0; i < N; i++) {
            cin >> arr[i];
            pq.push(arr[i]);
        }

        solve();
        memset(arr, 0, sizeof(arr));
        memset(tmp, 0, sizeof(tmp));
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
