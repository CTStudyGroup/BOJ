#include <iostream>
#include <utility>
using namespace std;

#define MAX 999999;
int d[21][2];
pair<int,int> v[21];
int main(){
    cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
    int n,k;
    cin >> n;

    for(int i = 1; i <n; i++){
        int v1,v2;
        cin >> v1 >> v2;
        v[i] = make_pair(v1,v2);
    }
    cin >> k;
    for(int i = 0; i<= n; i++) {
        d[i][0] = MAX;
        d[i][1] = MAX;
    }
    d[1][0] = 0;
    d[2][0]= v[1].first;
    d[3][0]= min(v[1].first+v[2].first,v[1].second);
    for(int i = 4; i <= n; i++){
        d[i][0] = min(v[i-1].first + d[i-1][0],v[i-2].second+d[i-2][0]);
        d[i][1] = min(min(v[i-1].first + d[i-1][1],v[i-2].second+d[i-2][1]),k+d[i-3][0]);
    }
    cout << min(d[n][0],d[n][1]);
}
