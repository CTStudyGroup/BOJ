#include <iostream>
#include <queue>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n,m;
char board[601][601]={0,};
int direct[4][2]={{-1,0},{0,-1},{1,0},{0,1}}; 
queue<point_t> q;
int visited[601][601];
int ans=0;

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
			if(board[i][j]=='I'){
				point_t temp={i,j};
				q.push(temp);
				visited[i][j]=true;
			}
		}
	}

}

void solve(){
	for(point_t temp=q.front();!q.empty();q.pop()){
		temp=q.front();
		point_t next;
		// cout<<temp.y<<" "<<temp.x<<"\n";
		for(int i=0;i<4;i++){
			next.y=temp.y+direct[i][0];
			next.x=temp.x+direct[i][1];

			if(next.y<0||next.x<0||next.y>=n||next.x>=m) continue;

			if(board[next.y][next.x]=='X') continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=1;
			q.push(next);
			if(board[next.y][next.x]=='P') ans++;

		}
	}
	if(ans==0) {
		cout<<"TT";
		return;
	}
	cout<<ans;
}

int main(){
	input();
	solve();
}