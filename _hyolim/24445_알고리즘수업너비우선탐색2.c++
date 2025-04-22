#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int n,m,r;
vector<int> vec[100001];
bool visited[100001];
int o[100001]={0,};

void input(){
	cin>>n>>m>>r;
	while(m--){
		int u,v;
		cin>>u>>v;
		vec[u].push_back(v);
		vec[v].push_back(u);	
	}

	for(int i=0;i<=n;i++){
		sort(vec[i].begin(),vec[i].end(),greater<int>());
	}
}

void solve(){
	queue<int> q;
	q.push(r);
	visited[r]=true;
	int cnt=1;
	for(int temp=q.front();!q.empty();q.pop()){
		temp=q.front();
		o[temp]=cnt;
		cnt++;
		for(auto e:vec[temp]){
			if(visited[e]) continue;
			visited[e]=true;
			q.push(e);
		}
	}
}

void output(){
	for(int i=1;i<=n;i++){
		cout<<o[i]<<"\n";
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	output();
}