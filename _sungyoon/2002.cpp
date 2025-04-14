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
int N;
map<string, int> m;
int arr[1001];
int result;

void solve() {
    for(int i = 1; i < N; i++) {
        for(int j = i + 1; j <= N; j++) {
            if(arr[i] > arr[j]) {
                result++;
                break;
            }
        }
    }

    cout << result;
}

void input() {
    cin >> N;

    for(int i = 1; i <= N; i++) {
        string s;
        cin >> s;
        m[s] = i;
    }

    for(int i = 1; i <= N; i++) {
        string s;
        cin >> s;
        arr[i] = m[s];
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
