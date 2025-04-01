#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
#define Endl "\n"
#define MAX 1e9

int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int C, P;
int arr[101];
int result;

void block1() {
    result = C + result;

    for(int i = 0; i < C - 3; i++) {
        if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2] && arr[i+2] == arr[i+3]) result++;
    }
}

void block2() {
    for(int i = 0; i < C - 1; i++) {
        if(arr[i] == arr[i+1]) result++;
    }
}

void block3() {
    for(int i = 0; i < C - 2; i++) {
        if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2] - 1) result++;
    }

    for(int i = 0; i < C - 1; i++) {
        if(arr[i] - 1 == arr[i+1]) result++;
    }
}

void block4() {
    for(int i = 0; i < C - 2; i++) {
        if(arr[i] - 1 == arr[i+1] && arr[i+1] == arr[i+2]) result++;
    }

    for(int i = 0; i < C - 1; i++) {
        if(arr[i] == arr[i+1] - 1) result++;
    }
}

void block5() {
    for(int i = 0; i < C - 2; i++) {
        if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2]) result++;
        if(arr[i] - 1 == arr[i+1] && arr[i] == arr[i+2]) result++;
    }

    for(int i = 0; i < C - 1; i++) {
        if(arr[i] == arr[i+1] - 1) result++;
        if(arr[i] - 1 == arr[i+1]) result++;
    }
}

void block6() {
    for(int i = 0; i < C - 2; i++) {
        if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2]) result++;
        if(arr[i] == arr[i+1] - 1 && arr[i+1] == arr[i+2]) result++;
    }

    for(int i = 0; i < C - 1; i++) {
        if(arr[i] == arr[i+1]) result++;
        if(arr[i] - 2 == arr[i+1]) result++;
    }
}

void block7() {
    for(int i = 0; i < C - 2; i++) {
        if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2]) result++;
        if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2] + 1) result++;
    }

    for(int i = 0; i < C - 1; i++) {
        if(arr[i] == arr[i+1] - 2) result++;
        if(arr[i] == arr[i+1]) result++;
    }
}

void solve() {
    if(P == 1) block1();
    else if(P == 2) block2();
    else if(P == 3) block3();
    else if(P == 4) block4();
    else if(P == 5) block5();
    else if(P == 6) block6();
    else block7();

    cout << result;
}

void input() {
    cin >> C >> P;

    for(int i = 0; i < C; i++) {
        cin >> arr[i];
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0), cout.tie(0);

    input();
    solve();
}

