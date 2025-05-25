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
string s;
bool visited[100];

/*
 *  보여주지 않은 문자열 중 추가했을때 사전 순으로 가장 앞에 오도록
 *
 *  재귀 한 기준으로 계속 오른쪽 탐색(없을 경우) 왼쪽 중 가장 작은거 기준 -> 오른쪽 탐색?
 *  재귀 타면서 가장 최소인지점 찾기?
 */

void bt(int start, int end) {
    char minchar = '~';
    int idx = -1;

    for (int i = start; i < end; i++) {
        if (minchar > s[i]) {
            minchar = s[i];
            idx = i;
        }
    }

    if (idx != -1) {
        visited[idx] = true;

        for (int i = 0; i < s.size(); i++) {
            if (visited[i]) {
                cout << s[i];
            }
        }
        cout << endl;

        bt(idx + 1, end);
        bt(start, idx);
    }
}


void solve() {
    bt(0, s.size());
}

void input() {
    cin >> s;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
