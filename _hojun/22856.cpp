#include <bits/stdc++.h>
using namespace std;

vector<int> graph[100001];
bool visited[1000001];
int end_node;
int ans = 0;
bool flag = true;
void go(int node) {

    int left_node = graph[node][0];     // 노드외 좌측 자식
    int right_node = graph[node][1];    // 노드의 우측 자식

    if (left_node != -1) {
        ans += 1;
        go(left_node);
        if (flag) ans += 1;
    }
    if (right_node != -1) {
        ans += 1;
        go(right_node);
        if (flag) ans += 1;
    }
    if (node == end_node) {
        flag = false;
        return;
    }
}

void inorder(int node) {
    int left_node = graph[node][0];
    int right_node = graph[node][1];

    if (left_node != -1) {
        inorder(left_node);
    }
    end_node = node;
    if (right_node != -1) {
        inorder(right_node);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N; cin >> N;
    for (int i = 0; i < N; i++) {
        int a, b, c; cin >> a >> b >> c;
        graph[a].push_back(b);
        graph[a].push_back(c);
    }
    inorder(1);  // 중위순회의 끝 노드를 찾음.
    go(1);   // 유사 중위순회 탐색
    cout << ans;
}