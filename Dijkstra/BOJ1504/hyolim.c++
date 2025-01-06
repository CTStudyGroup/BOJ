#include <iostream>
#include <queue>
#include <vector>
#include <functional>

using namespace std;

struct P{
	int w;
	int v;

	bool operator>(const P &other) const {
        return w > other.w;
    }
};

#define INF 0x3f3f3f3f
// 1base 코드

int n,e,fv,sv;
vector<P> adj[20005];
int d[20005];

void input(){
	ios::sync_with_stdio(0);
	cin.tie(0);

	cin>>n>>e;

	for(int i=0;i<e;i++){
		int v,e,w;
		cin>>v>>e>>w;
		P temp;
		temp.v=e;
		temp.w=w;
		P temp2;
		temp2.v=v;
		temp2.w=w;
		adj[v].push_back(temp);
		adj[e].push_back(temp2);
	}

	cin>>fv>>sv;

}

long dijkstra(int st,int fi){
	priority_queue <P,vector<P>,greater<P>> pq; // 계산에 사용할 큐
	fill(d,d+n+1,INF);

	d[st]=0; // 시작
	P temp={0,st};
	pq.push(temp);

	while(!pq.empty()){
		P cur = pq.top(); 
		pq.pop();
		// 최단거리 비교 : 최단 거리 테이블과 거리가 다를 경우 넘어감
		if(cur.w!=d[cur.v]) continue;

		for(auto nxt:adj[cur.v]){
			if(d[nxt.v]>d[cur.v]+nxt.w){
				d[nxt.v]=nxt.w+d[cur.v];
				P temp_a;
				temp_a.w=d[nxt.v];
				temp_a.v=nxt.v;
				pq.push(temp_a);
			}
		}
	}

	return d[fi];

}

void solve(){
	long ans1=dijkstra(1,fv)+dijkstra(fv,sv)+dijkstra(sv,n);
	long ans2=dijkstra(1,sv)+dijkstra(sv,fv)+dijkstra(fv,n);

	long ans=min(ans1,ans2);
	if(ans>=INF) ans =-1;
	cout<<ans;
}

int main(){
	input();
	solve();
}