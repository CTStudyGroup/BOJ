#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct point_t{
	int y;
	int x;
};

int r,c;
char board[251][251];
bool visited[251][251];
vector<point_t> wolf;
int dy[4]={0,0,-1,1};
int dx[4]={1,-1,0,0};

void input(){
	cin>>r>>c;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			cin>>board[i][j];
			if(board[i][j]=='v'){
				wolf.push_back({i,j});
			}
		}
	}
}

void bfs(int y,int x){
	if(visited[y][x]) return;
	visited[y][x]=true;

	queue<point_t> q;
	vector<point_t> wt; // 양의 개수
	vector<point_t> ot; // 늑대의 개수
	q.push({y,x});
	wt.push_back({y,x});

	for(;!q.empty();q.pop()){
		point_t temp= q.front();
		point_t next;

		for(int i=0;i<4;i++){
			next.y=temp.y+dy[i];
			next.x=temp.x+dx[i];

			if(next.y<0||next.x<0||next.y>=r||next.x>=c) continue;

			if(board[next.y][next.x]=='#') continue;

			if(visited[next.y][next.x]) continue;

			visited[next.y][next.x]=true;
			if(board[next.y][next.x]=='v') wt.push_back(next);
			if(board[next.y][next.x]=='o') ot.push_back(next);

			q.push(next);
		}
	}

	if(wt.size()<ot.size()){
		// 양이 많다면 늑대 전멸
		for(auto e:wt){
			board[e.y][e.x]='.';
		}
	}else{
		for(auto e:ot){
			board[e.y][e.x]='.';

		}
	}

}

void solve(){
	for(auto e:wolf){
		bfs(e.y,e.x);
	}
}

void output(){
	int scnt=0;
	int wcnt=0;

	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(board[i][j]=='v') wcnt++;
			if(board[i][j]=='o') scnt++;

		}
	}
	cout<<scnt<<" "<<wcnt;
}

int main(){
	input();
	solve();
	output();
}