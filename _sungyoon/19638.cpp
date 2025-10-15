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
int N, H, T;
priority_queue<int, vector<int>> pq;
int cnt;

/*
    YES일 경우 -> 최소 횟수 출력
    NO일 경우 -> T번 횟수 이후에 키가 가장 큰 거인 키 출력
*/

void solve() {
    bool flag = false;

    while(T--) {
        if(pq.top() == 1) {
            continue;
        }

        if(pq.top() < H) {
            flag = true;
            break;
        }

        int x = pq.top();
        pq.pop();
        x /= 2;
        pq.push(x);
        cnt++;
    }

    if(pq.top() < H) {
        flag = true;
    }

    if(flag) {      // 센티보다 다 작음
        cout << "YES" << endl << cnt;
    }
    else {
        cout << "NO" << endl << pq.top();
    }
}

void input() {
    cin >> N >> H >> T;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        pq.push(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

