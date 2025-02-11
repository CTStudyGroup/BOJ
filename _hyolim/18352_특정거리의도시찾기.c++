#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

// 출발한 도시에서 depth==k가 되면 도시의 번호를 출력
int n; // 도시의 개수
int m; // 도로의 개수
int k; // 거리 정보
int x; // 출발 도시 번호

int d[300001]; // 최단거리 배열
vector<int> vec[300001];

void input(){
	cin>>n>>m>>k>>x;
	for(int i=0;i<m;i++){
		int t1,t2;
		cin>>t1>>t2;
		vec[t1].push_back(t2);
	}

	// 최단거리 배열 초기화
	for(int i=1;i<=n;i++){
		d[i]=99999999;
	}
}

void dijkstra(int s){
	d[s]=0;
	queue<int> q;
	q.push(s);
	while(!q.empty()){
		int cur=q.front();
		q.pop();
		for(int i=0;i<vec[cur].size();i++){
			int next=vec[cur][i];
			if(d[next]>d[cur]+1){
				d[next]=d[cur]+1;
				q.push(next);
			}
		}
	}

}

void solve(){
	dijkstra(x);
	bool check=false;
	for(int i=1;i<=n;i++){
		if(d[i]==k){
			check=true;
			cout<<i<<"\n";
		}
	}
	if(!check) cout<<"-1";
}

int main(){
	input();
	solve();
}