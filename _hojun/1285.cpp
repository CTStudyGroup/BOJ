#include <bits/stdc++.h>

using namespace std;
int N;
int board[21][21];

int makeMinTail(int row) {
    int ret = 0;

    for (int j = 0; j < N; j++) {
        int headCnt = 0;

        for (int i = 0; i < N; i++) {
            bool head = board[i][j];
            if ((row & (1 << i)) != 0) head = !head;
            if (head) headCnt++;
        }

        ret += min(headCnt, N - headCnt);
    }

    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            char ch; cin >> ch;
            board[i][j] = ch == 'H' ? 1 : 0;
        }
    }

    int ans = 987654321;
    for (int i = 0; i < (1 << N); i++) {
        ans = min(ans, makeMinTail(i));
    }

    cout << ans;

	return 0; 
}