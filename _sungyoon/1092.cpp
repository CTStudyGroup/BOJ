#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e8

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 1, -1, 0, 1, -1, -1, 1};
int dy[] = {1, 0, 0, -1, -1, 1, -1, 1};
int N, M;
vector<int> crane;
vector<int> box;

bool compare(int a, int b) {
    return a > b;
}

void solve() {
    sort(crane.begin(), crane.end(), compare);
    sort(box.begin(), box.end(), compare);

    int cnt = 0;
    
    if(crane[0] < box[0]) {
        cout << -1;
        return;
    }

    while(!box.empty()) {
        cnt++;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < box.size(); j++) {
                if(crane[i] >= box[j]) {
                    box.erase(box.begin() + j);
                    break;
                }
            }
        }
    }

    cout << cnt;
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        int a;
        cin >> a;
        crane.push_back(a);
    }

    cin >> M;

    for(int i = 0; i < M; i++) {
        int a;
        cin >> a;
        box.push_back(a);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
