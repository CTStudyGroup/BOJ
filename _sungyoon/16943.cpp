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

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
string A, B;
int arr[10];
vector<int> v;
bool visited[10];
int tmparr[10];
int result;
bool flag1;

void bt(int cnt, int end) {
    if(cnt == end) {
        if(tmparr[0] == 0) return;
        string s = "";
        for(int i = 0; i < end; i++) {
            s += to_string(tmparr[i]);
        }
        int stand = stoi(B);
        int res = stoi(s);

        if(stand > res && stoi(A) != res) {       // 최댓값 update
            result = max(result, res);
            flag1 = true;
        }

        return;
    }

    for(int i = 0; i < A.size(); i++) {
        if(!visited[i]) {
            tmparr[cnt] = A[i] - '0';
            visited[i] = true;
            bt(cnt+1, end);
            visited[i] = false;
        }
    }
}

void solve() {
    bt(0, A.size());

    if(!flag1) {
        cout << -1;
    }
    else cout << result;
}

void input() {
    cin >> A >> B;

    for(int i = 0; i < A.size(); i++) {
        int a = A[i] - '0';
        arr[a]++;
        v.push_back(a);
    }

    bool flag = false;

    for(int i = 0; i < B.size(); i++) {
        int b = B[i] - '0';

        if(arr[b] != 0) {
            flag = true;
        }
    }

    if(flag) {
        solve();
    }
    else cout << -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
