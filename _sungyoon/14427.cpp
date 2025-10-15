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
int N, M;
int arr[100001];
priority_queue<pii, vector<pii>, greater<pii>> pq;

void solve() {
    for(int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a;

        if(a == 1) {
            cin >> b >> c;

            arr[b] = c;
            pq.push({c, b});
        }
        else {
            int idx = pq.top().second;
            int value = pq.top().first;

            while(arr[idx] != value) {
                pq.pop();
                idx = pq.top().second;
                value = pq.top().first;
            }

            idx = pq.top().second;

            cout << idx << endl;
        }
    }
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        cin >> arr[i];
        pq.push({arr[i], i});
    }

    cin >> M;

    solve();
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}

