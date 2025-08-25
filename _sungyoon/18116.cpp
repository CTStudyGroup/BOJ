#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define endl "\n"
#define MAX 1e11

struct coordinate {
    int x;
    int y;
};

int dx[] = {0, 0, -1, 1, 1, -1, -1, 1};
int dy[] = {-1, 1, 0, 0, -1, 1, -1, 1};
int N;
int unf[1000001];
int cnt[1000001];

int Find(int a) {
    if(a == unf[a]) return a;
    return unf[a] = Find(unf[a]);
}

void Union(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(a > b) {
        unf[a] = b;
        cnt[b] += cnt[a];
        cnt[a] = 0;
    }
    else {
        unf[b] = a;
        cnt[a] += cnt[b];
        cnt[b] = 0;
    }
}

bool isUnion(int a, int b) {
    a = Find(a);
    b = Find(b);

    if(a == b) return true;
    else return false;
}

void Init() {
    for(int i = 1; i <= 1000000; i++) {
        unf[i] = i;
        cnt[i] = 1;
    }
}

void input() {
    cin >> N;

    Init();

    for(int i = 0; i < N; i++) {
        char a;

        cin >> a;

        if(a == 'I') {
            int b, c;
            cin >> b >> c;

            if(!isUnion(b, c)) {
                Union(b, c);
            }
        }
        else {
            int b;
            cin >> b;

            cout << cnt[Find(unf[b])] << endl;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();

}
