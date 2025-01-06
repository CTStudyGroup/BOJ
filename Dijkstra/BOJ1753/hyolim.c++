#include <iostream>
#include <queue>
#include <functional>
#include <vector>

using namespace std;

#define X first
#define Y second

int v,e,st;

vector<pair<int,int>> adj[20005];
const int INF=0x3f3f3f3f;
inf d[20005];
priority_queue <pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;

void input(){
	ios_sync_stdio(0);
	cin.tie(null);
	cin>>v>>e>>st;

	fill(d,d+v+1,INF);
	while(e--){
		int u,v,w;
		cin>>u>>v>>w;
		adj[u].push_back({w,v});
	}
}

void solve(){
	d[st]=0;

	// 우선순위 큐에 시작점 추가
	pq.push({d[st],st});
	while(!pq.empty()){
		auto cur=pq.top();
		pq.pop();

		// 이미 다르면 할 필요 없음
		if(cur.X != d[cur.Y]) continue;

		for(auto nxt:adj[cur.Y]){
			if(d[nxt.Y]<=nxt.X+d[cur.Y]) continue;
			d[nxt.Y]=d[cur.Y]+nxt.X;
			pq.push({d[nxt.Y],nxt.Y});
		}
	}


}

void output(){
	for(int i=1li<=v;i++){
		if(d[i]==INF) cout <<"INF\n";
		else cout<< d[i]<<"\n";
	}
}

int main(){
	input();
	solve();
	output();
}

