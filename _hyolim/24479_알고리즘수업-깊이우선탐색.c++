#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n,m,r;
vector<int> graph[100002];
bool visited[100002];
int answer[100002]={0,};
int cnt=1;
void input(){
	cin>>n>>m>>r;

	for(int i=0;i<m;i++){
		int u,v; cin>>u>>v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
}

void dfs(int depth,int node){
	answer[node]=cnt;
	cnt++;

	if(depth==n){
		return;
	}
	for(auto e:graph[node]){
		if(visited[e]) continue;
		visited[e]=true;
		dfs(depth+1,e);
	}
}

void solve(){
	for(int i=1;i<=n;i++){
		if(graph[i].empty()) continue;
		sort(graph[i].begin(),graph[i].end());
	}	
	visited[r]=true;
	dfs(0,r);
}

void output(){
	for(int i=1;i<=n;i++){
		cout<<answer[i]<<"\n";
	}
}

int main(){
	input();
	solve();
	output();

}