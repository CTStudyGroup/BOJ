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
int N;
int graph[51][51];


void Init() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            if(i == j) continue;
            graph[i][j] = MAX;
        }
    }
}

void Print() {
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

void solve() {
    for(int k = 1; k <= N; k++) {
        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= N; j++) {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }

    vector<int> v;
    int max_value = MAX;

    for(int i = 1; i <= N; i++) {
        int min_num = 0;
        for(int j = 1; j <= N; j++) {
            min_num = max(min_num, graph[i][j]);
        }

        if(max_value >= min_num) {
            if(max_value == min_num) {      // 같은 경우
                v.push_back(i);
                max_value = min_num;
            }
            else {
                v.clear();
                v.push_back(i);
                max_value = min_num;
            }
        }
    }

    cout << max_value << " " << v.size() << endl;

    for(auto it : v) {
        cout << it << " ";
    }
}

void input() {
    cin >> N;

    Init();

    while(true) {
        int a, b;
        cin >> a >> b;

        if(a == -1 && b == -1) break;
        graph[a][b] = 1;
        graph[b][a] = 1;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

