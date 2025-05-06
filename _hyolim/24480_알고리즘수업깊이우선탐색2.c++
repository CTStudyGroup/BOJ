#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n,m,r;

vector<int> graph[100001];
int visited[100001]={0,};
int cnt=1;

void input(){
	cin>>n>>m>>r;
	for(int i=0;i<m;i++){
		int u,v;
		cin>>u>>v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
}

void dfs(int temp){
	visited[temp]=cnt;
	for(auto e:graph[temp]){
		if(visited[e]) continue;
		cnt++;
		dfs(e);
	}
}

void solve(){
	// 내림차순 정렬
	for(int i=1;i<=n;i++){
		sort(graph[i].begin(),graph[i].end(),greater<int>());
	}

	// for(int i=1;i<=n;i++){
	// 	for(auto e:graph[i]){
	// 		cout<<e<<" ";
	// 	}
	// 	cout<<"\n";
	// }
	// 1base인거 까먹지 말기
	dfs(r);
}

void output(){
	for(int i=1;i<=n;i++){
		cout<<visited[i]<<"\n";
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	output();
}