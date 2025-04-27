#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1 ,1, 0, 0};
int dy[] = {0, 0, -1, 1};
int T, K;
string graph[1001];
int visited[1001];

void rotate1(int stand) {       // 시계방향
    string tmp = graph[stand];

    char tmp1 = tmp[7];
    tmp = tmp.substr(0, 7);
    string result = string(1, tmp1) + tmp;
    graph[stand] = result;
}

void rotate2(int stand) {       // 반시계
    string tmp = graph[stand];

    char tmp1 = tmp[0];
    tmp = tmp.substr(1, 7);
    string result = tmp + string(1, tmp1);
    graph[stand] = result;
}

void search(int a, int b) {
    if(a == 1) {        // 오른쪽만 보면 됨
        visited[a] = b;
        for(int i = 2; i <= T; i++) {
            if(graph[i-1][2] != graph[i][6]) {      // N극과 S극이 다른경우
                visited[i] = visited[i-1] * -1;
            }
            else break;
        }
    }
    else if(a == T) {       // 왼쪽만 보면됨
        visited[a] = b;
        for(int i = T; i > 1; i--) {
            if(graph[i][6] != graph[i-1][2]) {
                visited[i-1] = visited[i] * -1;
            }
            else break;
        }
    }
    else {      // 왼쪽 오른쪽 다봐야함
        visited[a] = b;
        for(int i = a; i > 1; i--) {        // 왼쪽 보기
            if(graph[i][6] != graph[i-1][2]) {
                visited[i-1] = visited[i] * -1;
            }
            else break;
        }

        for(int i = a; i < T; i++) {        // 오른쪽 보기
            if(graph[i][2] != graph[i+1][6]) {
                visited[i+1] = visited[i] * -1;
            }
            else break;
        }
    }

    for(int i = 1; i <= T; i++) {
        if(visited[i] == 1) {
            rotate1(i);
        }
        else if(visited[i] == -1) {
            rotate2(i);
        }
    }

    memset(visited, 0, sizeof(visited));
}

void solve() {
    int cnt = 0;

    for(int i = 1; i <= T; i++) {
        if(graph[i][0] == '1') {
            cnt++;
        }
    }

    cout << cnt;
}

void input() {
    cin >> T;

    for(int i = 1; i <= T; i++) {
        cin >> graph[i];
    }

    cin >> K;

    for(int i = 0; i < K; i++) {
        int a, b;
        cin >> a >> b;
        search(a, b);
    }

    solve();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
}
