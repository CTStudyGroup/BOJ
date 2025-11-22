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

struct halloween {
    int cnt;
    int score;
};

// int dx[] = {-1, 1, 0, 0, 1, -1, -1, 1};
// int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
int N;
int InOrder[100001];
int PostOrder[100001];
int Index[100001];

void PreOrder(int instart, int inend, int poststart, int postend) {
    if(instart > inend || poststart > postend) return;

    int root = PostOrder[postend];
    int rootidx = Index[root];
    int leftsize = rootidx - instart;
    int rightsize = inend - rootidx;

    cout << root << ' ';

    PreOrder(instart, rootidx-1, poststart, poststart + leftsize-1);      // 왼쪽 서브트리
    PreOrder(rootidx+1, inend, poststart + leftsize, postend-1);      // 오른쪽 서브트리
}

void solve() {
    PreOrder(0, N-1, 0, N-1);
}

void input() {
    cin >> N;

    for(int i = 0; i < N; i++) {
        cin >> InOrder[i];
        Index[InOrder[i]] = i;
    }

    for(int i = 0; i < N; i++) {
        cin >> PostOrder[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

