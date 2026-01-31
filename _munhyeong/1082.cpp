#include <iostream>
#include <queue>
#include <string>
 
#define kit ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
 
using namespace std;
typedef pair<int,int> pii;
 
priority_queue<pii, vector<pii>, greater<pii>> mi;
int n, m, p[50], c[50], cnt=0;
string ans = "";
 
int main() {
    kit cin >> n;
    for (int i=0; i<n; i++) {
        cin >> p[i];
        mi.push({p[i], i});
    }
    cin >> m;
    
    pii cur = mi.top(); // 가장 싼방번호 저장
    if (cur.second == 0) {
        mi.pop();
        if (mi.top().first > m) { //구매할 수 없을 때 0
            cout << 0;
            return 0;
        }
    }
    
    m -= mi.top().first; c[cnt] = mi.top().first;
    ans += to_string(mi.top().second);
    cnt++;
    
    while (m >= cur.first) { // 제일 싼 거로 남은 부분 모두 채워줌
        m -= cur.first;
        ans += to_string(cur.second);
        c[cnt] = cur.first; cnt++;
    }
 
    int j=0;
    // 앞에서부터 큰 수로 바꿀 수 있는지 확인해줌
    // 더이상 구매할 수 없을 때, 범위를 나갔을 때,
    while(j < ans.length())
    {
        for (int i=n-1; i>0; i--)
        {
            // 구매할 필요가 없는 경우
            if ((int)ans[j] - '0' >= i) break;
            if (m + c[j] >= p[i]) { // 갱신할 돈을 구매할 수 있으면 구매함
                ans[j] = (char)(i + 48);
                m = m - (p[i] - c[j]);
                c[j] = p[i];
                break;
            }
        }
        j++;
    }
    
    for (char a : ans) cout << a;
}