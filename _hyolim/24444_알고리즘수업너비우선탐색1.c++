#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n;
int m;
vector<int> vec[100001];
int r;
int visited[100001]={0,};

void input(){
	cin>>n>>m>>r;

	for(int i=0;i<m;i++){
		int u,v;
		cin>>u>>v;
		vec[u].push_back(v);
		vec[v].push_back(u);
	}
}

void solve(){
	queue<int> q;
	q.push(r);
	visited[r]=1;
	for(int i=1;i<=n;i++){
		sort(vec[i].begin(),vec[i].end());
	}
	int cnt=1;
	int temp;
	for(temp=q.front();!q.empty();q.pop()){
		temp=q.front();
		int next;
		for(auto e:vec[temp]){
			next=e;
			if(visited[next]) continue;
			visited[next]=++cnt;
			q.push(next);
		}
	}
}

void output(){
	for(int i=1;i<=n;i++){
		cout<<visited[i]<<"\n";
	}
}

int main(){
	input();
	solve();
	output();
}