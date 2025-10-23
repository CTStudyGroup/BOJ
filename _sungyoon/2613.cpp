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

struct horse {
    int x;
    int y;
    int dir;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
// int dx[] = {0, 0, 1, -1};
// int dy[] = {1, -1, 0, 0};
int dx[] = {1, 1, 1};
int dy[] = {-1, 0, 1};
int N, M;
int arr[301];

bool check(int mid) {
    int groups = 1;
    int sum = 0;

    for(int i = 0; i < N; i++) {
        if(arr[i] > mid) return false;

        if(sum + arr[i] > mid) {        // 중간값보다 큰 경우 그룹 나눠줘야함
            groups++;
            sum = arr[i];
        }
        else sum += arr[i];
    }

    return groups <= M;
}

void solve() {
    int left = 0;
    int right = 1e9;

    while(left +1 < right) {
        int mid = (left + right) / 2;

        if(check(mid)) {
            right = mid;
        }
        else {
            left = mid;
        }
    }

    cout << right << endl;

    int sum = 0;
    int cnt = 0;
    for(int i = 0; i < N; i++) {
        sum += arr[i];
        if(sum > right) {
            sum = arr[i];
            M--;
            cout << cnt << " ";
            cnt = 0;
        }
        cnt++;
        if(N - i == M) break;
    }
    while(M--) {
        cout << cnt << " ";
        cnt = 1;
    }
}

void input() {
    cin >> N >> M;

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

