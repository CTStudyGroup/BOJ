#include <bits/stdc++.h>
#define endl "\n"
#define rep(i, a, b) for(auto i = a; i < b; ++i)
#define rrep(i, a, b) for(auto i = a; i > b; --i)
#define REP(i, a, b) for(auto i = a; i <= b; ++i)
#define RREP(i, a, b) for(auto i = a; i >= b; --i)
#define ll long long

using namespace std;

int dx[8] = { -1, -1, -1, 0, 0, 1, 1, 1 };
int dy[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };


int main() {
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    int N, M, K; cin >> N >> M >> K;

    vector<vector<int>> ground(N, vector<int>(N, 5));
    vector<vector<int>> A(N, vector<int>(N, 0));
    vector<int> trees[11][11];

    rep(i, 0, N) {
        rep(j, 0, N) {
            cin >> A[i][j];
        }
    }

    rep(i, 0, M) {
        int a, b, c;
        cin >> a >> b >> c;
        trees[a - 1][b - 1].push_back(c);
    }

    while (K--)
    {
        rep(i, 0, N) {
            rep(j, 0, N) {
                vector<int> alive;
                int dead = 0;

                sort(trees[i][j].begin(), trees[i][j].end());

                for (int age : trees[i][j]) {
                    if (ground[i][j] >= age) { // 살아남음
                        ground[i][j] -= age;
                        alive.push_back(age + 1);
                    }
                    else {
                        dead += age / 2;
                    }
                }

                trees[i][j] = alive;       // 살아남은 나무 갱신
                ground[i][j] += dead;  // 여름 처리
            }
        }

        //가을 처리
        vector<pair<int, int>> newTrees;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int age : trees[i][j]) {
                    if (age % 5 == 0) {
                        newTrees.push_back({ i, j });
                    }
                }
            }
        }

        for (auto& point : newTrees) {
            int x = point.first;
            int y = point.second;

            for (int d = 0; d < 8; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

                trees[nx][ny].push_back(1);
            }
        }

        //겨울 처리
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                ground[i][j] += A[i][j];
    }

    int ans = 0;
    rep(i, 0, N) {
        rep(j, 0, N) {
            ans += trees[i][j].size();
        }
    }

    cout << ans;

    return 0;
}
