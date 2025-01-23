#include <iostream>
#include <vector>
using namespace std;

int n;
vector<pair<int,int>> tree[10002];
bool visited[10002];
int ans=0;
int endP;

void input(){
	cin >> n;
	for(int i=0;i<n-1;i++){
		int p,c,w;
		cin>>p>>c>>w;
		tree[p].push_back({c,w});
		tree[c].push_back({p,w});
	}
}


void dfs(int node,int num){
	visited[node]=1;
	if(ans<num) {
		ans=num;
		endP=node;
	}


	for(int i=0;i<tree[node].size();i++){
		// visited 확인
		if(visited[tree[node][i].first]) continue;
		dfs(tree[node][i].first,num+tree[node][i].second);
	}
}

void solve(){
	dfs(1,0);
	ans=0;
	for(int i=0;i<=n;i++){
		visited[i]=false;
	}
	dfs(endP,0);
	cout<<ans;

}

int main(){
	input();
	// printTree();
	solve();
	// output();
}