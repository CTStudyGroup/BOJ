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
int dx[] = {1, 0};
int dy[] = {0, 1};
int N;
vector<pii> v;
priority_queue<int, vector<int>> pq[100001];
map<string, int> m;
ll answer = 0;

void solve() {

}

void input() {
    int namecnt = 0;
    cin >> N;

    for(int i = 0; i < N; i++) {
        string name;
        int query;
        int k;

        cin >> query;

        if(query == 1)  {       // 정보 저장
            cin >> name >> k;

            if(m.find(name) == m.end()) {       // 정보 없음
                m[name] = namecnt++;
            }
            int idx = m[name];

            for(int j = 0; j < k; j++) {
                int a;
                cin >> a;
                pq[idx].push(a);
            }
        }
        else {
            cin >> name >> k;

            if(m.find(name) == m.end()) {
                continue;
            }
            int idx = m[name];

            if(pq[idx].size() < k) {
                while(!pq[idx].empty()) {
                    answer += pq[idx].top();
                    pq[idx].pop();
                }
            }
            else {
                for(int i = 0; i < k; i++) {
                    answer += pq[idx].top();
                    pq[idx].pop();
                }
            }
        }
    }

    cout << answer;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

