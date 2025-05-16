#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

struct point_t{
	int y;
	int x;
};

int n; // 보드 크기
int q; // 총 몇 번 반복
vector<int> vecL;
vector<vector<int>> board;
int dy[4]={0,0,-1,1};
int dx[4]={1,-1,0,0};
int visited[100][100]={0,};
int N=0;

void printB(vector<vector<int>> v){
	cout<<"---board---\n";
	for(auto e:v){
		for(auto u:e){
			cout<<u<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>q;
	N=1<<n;
	for(int i=0;i<N;i++){
		vector<int> vectemp;
		for(int j=0;j<N;j++){
			int temp; cin>>temp;
			vectemp.push_back(temp);

		}
		board.push_back(vectemp);

	}

	for(int i=0;i<q;i++){
		int temp; cin>>temp;
		vecL.push_back(temp);
	}

	// printB(board);
	// for(auto e:vecL) cout<<e<<" ";
}

vector<vector<int>> turn(vector<vector<int>> v) {
	int vn = v.size();
	vector<vector<int>> temp(vn, vector<int>(vn));

	for(int i = 0; i < vn; i++) {
		for(int j = 0; j < vn; j++) {
			temp[j][vn - 1 - i] = v[i][j];
		}
	}

	// cout << "--- before ---\n";
	// printB(v);
	// cout << "--- after ---\n";
	// printB(temp);

	return temp;
}

// 3. 이후 얼음이 있는 칸(3이상)과 인접해있지 않은 칸은 얼음이 1 줄어든다.
// (r,c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다.
void shrink(){
	vector<vector<int>> tempboard=board;
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			// 주변에 3이상 얼음이 있는지 확인
			int cnt=0;
			for(int k=0;k<4;k++){
				int ny=i+dy[k];
				int nx=j+dx[k];

				if(ny<0||nx<0||ny>=N||nx>=N) continue;
				if(board[ny][nx]>0) cnt++;
			}

			if(cnt<3){
				if(board[i][j]==0) continue;
				tempboard[i][j]--;
			}
		}
	}
	board=tempboard;
}

void solve(){
	// 1. 격자를 2^L, 2^L 크기의 부분 격자로 나눈다.
	for(auto e:vecL){
		int E=1<<e;
		// 쪼개기
		for(int i=0;i<=N-E;i+=E){
			for(int j=0;j<=N-E;j+=E){
				// cout<<i<<","<<j<<"\n";
				// pow(2,e) 만큼 
				vector<vector<int>> tempv;
				for(int y=i;y<i+E;y++){
					vector<int> tv;
					for(int x=j;x<j+E;x++){
						tv.push_back(board[y][x]);
					}
					tempv.push_back(tv);
				}

				// 2. 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
				// 변환 후 v에 적용
				tempv=turn(tempv);

				for(int y=i;y<i+E;y++){
					vector<int> tv;
					for(int x=j;x<j+E;x++){
						board[y][x]=tempv[y-i][x-j];
					}
				}

			}
		}
		// printB(board);
		shrink();
		// cout<<"===shrink===\n";
		// printB(board);
	}
}

long getsum(){
	long answer=0;
	for(auto e:board){
		for(auto u:e){
			answer+=u;
		}
	}
	return answer;
}

int bfs(int y,int x,int N){
	int s=1;
	visited[y][x]=1;
	queue<point_t> q;
	q.push({y,x});

	for(;!q.empty();q.pop()){
		point_t temp=q.front();
		point_t next;
		for(int i=0;i<4;i++){
			next.y=temp.y+dy[i];
			next.x=temp.x+dx[i];

			if(next.y<0||next.x<0||next.y>=N||next.x>=N) continue;
			if(visited[next.y][next.x]) continue;
			if(!board[next.y][next.x]) continue;

			s++;
			visited[next.y][next.x]=1;
			q.push(next);
		}
	}
	return s;
}

int getdong(){
	int maxsize=0;

 	for(int i=0;i<N;i++){
 		for(int j=0;j<N;j++){
 			if(visited[i][j]) continue;
 			if(!board[i][j]) continue;
 			maxsize=max(maxsize,bfs(i,j,N));
 		}
 	}
	return maxsize;
}

void output(){
	// 남아있는 얼음의 합
	cout<<getsum()<<"\n";

	// 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
	// 얼음이 있는 칸끼리 인접해있으면 두 칸은 연결되어있다. 덩어리는 연결된 칸의 집합이다. 
	cout<<getdong();
}

int main(){
	input();
	solve();
	output();
}