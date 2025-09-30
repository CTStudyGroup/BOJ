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
vector<pii> v;
int visited[1001];

bool compare(pii a, pii b) {
    if(a.second == b.second) {
        return a.first > b.first;
    }
    else return a.second > b.second;
}

void solve() {
    sort(v.begin(), v.end(), compare);

    int answer = 0;
    for(int i = 0; i < N; i++) {
        int endDay = v[i].first;
        int score = v[i].second;

        for(int j = endDay; j >= 1; j--) {
            if(visited[j]) {
                continue;
            }
            else {
                answer += score;
                visited[j] = true;
                break;
            }
        }
    }

    cout << answer;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, b});
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

