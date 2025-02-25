#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int N,M,order;
vector<int> down[501];
vector<int> up[501];
int check[501];

void dfs(vector<int> v[],int start){
	check[start]=1;
	for(int i=0;i<v[start].size();i++){
		int x=v[start][i];
		if(check[x]==0){
			check[x]=1;
			order++;
			dfs(v,x);
		}
	}
}

void solve(){
	int ans=0;
	for(int i=1;i<=N;i++){
		order=0;
		memset(check,0,sizeof(check));
		dfs(down,i);
		memset(check,0,sizeof(check));
		dfs(up,i);		
		if(order==N-1) ans++;
	}
	cout<<ans;
}
int main(){
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M;
    for(int i = 1; i <= M; i++){
        int x, y;
        cin >> x >> y;
        down[y].push_back(x);
        up[x].push_back(y);
    }
    solve();
    return 0;
}