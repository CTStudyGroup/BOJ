#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

struct point_t{
	int y;
	int x;
	int val;

	bool operator<(const point_t& o)const{
		if(val==o.val){
			return y<o.y;
		}
		return val>o.val;
	}
};

int dy[8]={-1,-1,-1,0,0,1,1,1};
int dx[8]={-1,0,1,-1,1,-1,0,1};

int n,m;
int board[101][71]={0,};
bool visited[101][71];
long answer=0;
vector<point_t> vec;

void input(){
	cin>>n>>m;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
			vec.push_back({i,j,board[i][j]});
		}
	}

}

void bfs(int y,int x){
	queue<point_t> q;
	q.push({y,x,board[y][x]});
    visited[y][x]=1;

    // cout<<"--- \n";

	for(point_t temp;!q.empty();q.pop()){
		temp=q.front();
		point_t next;
		// cout<<temp.y<<" "<<temp.x<<"\n";
		for(int i=0;i<8;i++){
			next.y=temp.y+dy[i];
			next.x=temp.x+dx[i];

			if(next.y<0||next.x<0||next.y>=n||next.x>=m) continue;

			if(board[next.y][next.x]>board[temp.y][temp.x]) continue;
			if(board[next.y][next.x]==0) continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=true;
			q.push(next);
		}
	}
    // cout<<"=== \n";

}

// 산봉우리 : 같은 높이를 갖는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어진 것
// 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
// bfs로 얼마나 많은 덩어리가 있는지 확인하기
void solve(){
	sort(vec.begin(),vec.end());
	for(auto e:vec){
		// cout<<e.y<<" "<<e.x<<"\n";
		if(visited[e.y][e.x]==0&&board[e.y][e.x]!=0){
			// cout<<"*"<<"\n";
			answer++;
			bfs(e.y,e.x);
		}
	}

	cout<<answer;
}

int main(){
	input();
	solve();
}