#include <bits/stdc++.h>
using namespace std;

struct river
{
    int order;
    int cnt;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int T; cin >> T;

    while (T--)
    {
        int k, m, p; cin >> k >> m >> p;
        vector<river> Nodes(m + 1, { 1, 0 });
        vector<int> orders(m + 1, 1);
        vector<vector<int>> graph(m + 1);
        vector<int> inter(m + 1);

        for (int i = 0; i < p; i++) {
            int a, b; cin >> a >> b;
            graph[a].push_back(b);
            inter[b]++;
        }

        //진입 차수가 0인 노드를 큐에 넣기
        queue<int> q;
        for (int i = 1; i <= m; ++i) {
            if (inter[i] == 0) {
                q.push(i);
            }
        }
        //큐에서 나올때는 내가 무슨 순서인지 확인하고 나올것
        while (!q.empty())
        {
            int CurNode = q.front();
            q.pop();

            int curCnt = Nodes[CurNode].cnt;
            int curOrder = Nodes[CurNode].order;

            if (curCnt <= 1) {
                orders[CurNode] = curOrder;
            }
            else {
                orders[CurNode] = curOrder + 1;
            }

            cout << CurNode << " : " << curOrder << " " << curCnt <<" " << orders[CurNode] << endl;

            for (auto& a : graph[CurNode]) {
                if (Nodes[a].order < orders[CurNode]) {
                    Nodes[a].order = orders[CurNode];
                    Nodes[a].cnt = 1;
                }
                else if (Nodes[a].order == orders[CurNode]) {
                    Nodes[a].cnt++;
                }

                inter[a]--;
               
                //차수가 0이 되면 큐에 push하기
                if (inter[a] == 0) {
                    q.push(a);
                }
            }
        }
        cout << k << " " << orders[m];
    }

    return 0;
}