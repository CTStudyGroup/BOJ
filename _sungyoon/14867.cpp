#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int a, b, c, d;
map<pii, int> m;

bool check(int x, int y) {
    if(m.find({x, y}) != m.end()) {         // 이미 있는 경우
        return false;
    }

    if(x > a || y > b || x < 0 || y < 0) return false;
    return true;
}

void bfs() {
    queue<tuple<int, int, int>> q;
    m[{0, 0}] = 1;
    q.push({0, 0, 0});          // a 물통 양, b 물통 양, 횟수

    while(!q.empty()) {
        int x = get<0>(q.front());
        int y = get<1>(q.front());
        int cnt = get<2>(q.front());
        q.pop();

        if(c == x && d == y) {
            cout << cnt;
            exit(0);
        }

        for(int i = 0; i < 3; i++) {
            if(i == 0) {        // 물 채우기
                for(int j = 0; j < 2; j++) {
                    if(j == 0) {
                        int nx = a;
                        int ny = y;

                        if(check(nx, ny)) {
                            q.push({nx, ny, cnt+1});
                            m[{nx, ny}] = 1;
                        }
                    }
                    else {
                        int nx = x;
                        int ny = b;

                        if(check(nx, ny)) {
                            q.push({nx, ny, cnt+1});
                            m[{nx, ny}] = 1;
                        }
                    }
                }
            }
            else if(i == 1) {       // 물 버리기
                for(int j = 0; j < 2; j++) {
                    if(j == 0) {
                        int nx = 0;
                        int ny = y;

                        if(check(nx, ny)) {
                            q.push({nx, ny, cnt+1});
                            m[{nx, ny}] = 1;
                        }
                    }
                    else {
                        int nx = x;
                        int ny = 0;

                        if(check(nx, ny)) {
                            q.push({nx, ny, cnt+1});
                            m[{nx, ny}] = 1;
                        }
                    }
                }
            }
            else {              // 물 옮기기
                int pour1 = min(x, b - y);
                int nx1 = x - pour1;
                int ny1 = y + pour1;

                if(check(nx1, ny1)) {
                    q.push({nx1, ny1, cnt+1});
                    m[{nx1, ny1}] = 1;
                }

                int pour2 = min(y, a - x);
                int nx2 = x + pour2;
                int ny2 = y - pour2;

                if(check(nx2, ny2)) {
                    q.push({nx2, ny2, cnt+1});
                    m[{nx2, ny2}] = 1;
                }
            }
        }
    }
}

void solve() {
    bfs();

    cout << -1;
}

void input() {
    cin >> a >> b >> c >> d;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
