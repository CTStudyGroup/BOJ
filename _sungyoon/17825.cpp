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
int arr[10];
int Map[33];
int Pos[4];
int score[33];      // 칸에 대한 점수
bool check[33];     // 칸에 말이 있는지
int direct[33];     // 파란색 원 방향
int result;

void bt(int cnt, int sum) {
    if(cnt == 10) {
        result = max(result, sum);
        return;
    }

    for(int i = 0; i < 4; i++) {
        int position = Pos[i];
        int tmp = position;
        int dir_cnt = arr[cnt];

        if(direct[tmp] > 0) {
            tmp = direct[tmp];
            dir_cnt--;
        }

        while(dir_cnt--) {
            tmp = Map[tmp];
        }

        if(tmp != 21 && check[tmp]) continue;

        Pos[i] = tmp;
        check[position] = false;
        check[tmp] = true;

        bt(cnt+1, sum + score[tmp]);

        check[position] = true;
        check[tmp] = false;
        Pos[i] = position;
    }
}

void solve() {
    bt(0, 0);

    cout << result;
}

void input() {
    for(int i = 0; i < 10; i++) {
        cin >> arr[i];
    }

    for(int i = 0; i < 21; i++) {
        Map[i] = i+1;
    }
    Map[21] = 21;

    for(int i = 22; i < 27; i++) {
        Map[i] = i+1;
    }
    Map[27] = 20, Map[28] = 29, Map[29] = 30, Map[30] = 25;
    Map[31] = 32, Map[32] = 25;

    direct[5] = 22, direct[10] = 31, direct[15] = 28;

    for(int i = 0; i < 21; i++) {
        score[i] = i * 2;
    }
    score[22] = 13, score[23] = 16,  score[24] = 19, score[25] = 25;
    score[26] = 30, score[27] = 35, score[28] = 28, score[29] = 27, score[30] = 26;
    score[31] = 22, score[32] = 24;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}
