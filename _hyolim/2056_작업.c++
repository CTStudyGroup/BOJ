#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n;
int deg[10002];
int dur[10002];
vector<int> adj[32001];
vector<int> tt[1000002];
long ans=0;
int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin>>n;

	for(int i=1;i<=n;i++){
		int m; cin>>dur[i]>>m;

		// 맨 첫번째 것만 넣기
		if(!m) tt[dur[i]].push_back(i);

		while(m--){
			int temp; cin>>temp;
			adj[temp].push_back(i);
			deg[i]++;
		}

	}

	for(int t=0;t<=1000000;t++){
		for(int finished:tt[t]){ // tt에 있어야 실행할 수 있또록 함. tt에 없는데도 실행 가능한건 좀
			ans=t;
			for(int r:adj[finished]){
				deg[r]--;
				if(deg[r]!=0) continue; // 선행 작업이 남아있을 경우 그냥 냅두기
				tt[t+dur[r]].push_back(r); // 선행 작업이 완료될 경우 tt 배열에 추가하기
			}
		}
	}
	cout<<ans;
}