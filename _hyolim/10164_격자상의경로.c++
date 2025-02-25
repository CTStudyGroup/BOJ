#include <iostream>
#include <cstring>
using namespace std;

bool visited[16][16]={0,};
int n,m,k;
int ky=-1,kx=-1;
int direct[2][2]={{1,0},{0,1}};
long ans=0;
long ans1=0;
long ans2=0;

void input(){
	cin>>n>>m>>k;
	if(k==0) return;
	if(k%m==0) {
		ky=k/m-1;
		kx=m-1;
	}
	else{
		ky=k/m;
		kx=(k%m)-1;
	}
	// cout<<ky<<" "<<kx<<"\n";
}

void dfs(int tempy,int tempx,int finy,int finx){
	// cout<<tempy<<" "<<tempx<<" "<<finy<<" "<<finx<<"\n";

	if(tempy==finy&&tempx==finx){
		// cout<<"*";
		ans++;
		return;
	}
	for(int i=0;i<2;i++){
		int nexty=tempy+direct[i][0];
		int nextx=tempx+direct[i][1];
		if(nexty<0||nextx<0||nexty>=n||nextx>=m) continue;
		if(!visited[nexty][nextx]){
			visited[nexty][nextx]=true;
			dfs(nexty,nextx,finy,finx);
			visited[nexty][nextx]=false;
		}
	}
}

void solve(){
	if(k==0){
		// cout<<"!";
		dfs(0,0,n-1,m-1);
		cout<<ans;
		return;
	}
	dfs(0,0,ky,kx);
	ans1=ans;
	ans=0;
	memset(visited,0,sizeof(visited));
	dfs(ky,kx,n-1,m-1);
	ans2=ans;
	cout<<ans1*ans2;
}
int main(){
	input();
	solve();
}