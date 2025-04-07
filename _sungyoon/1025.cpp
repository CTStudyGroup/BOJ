#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e9

struct coordinate {
    int x, y;
};

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int N, M;
string graph[9][9];
int result = -1;

int convert(string s) {
    if(s[0] == '0') {
        return 0;
    }
    return stoi(s);
}

bool square(int a) {
    int tmp = sqrt(a);

    if(tmp * tmp == a) {
        return true;
    }
    return false;
}

void solve() {
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            for(int k = -N; k < N; k++) {
                for(int l = -M; l < M; l++) {
                    int x, y;
                    x = i;
                    y = j;

                    if(k == 0 && l == 0) continue;

                    string s;
                    while(0 <= x && 0 <= y && x < N && y < M) {
                        s += graph[x][y];


                        int res = convert(s);

                        if(square(res)) {
                            result = max(res, result);
                        }

                        x += k;
                        y += l;
                    }
                }
            }
        }
    }

    cout << result;
}

void input() {
    cin >> N >> M;

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {
            char a;
            cin >> a;
            graph[i][j] = a;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
