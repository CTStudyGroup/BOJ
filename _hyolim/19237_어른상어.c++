#include <iostream>
#include <vector>

using namespace std;

// 상어는 1base
struct shark{
	int idx; // 상어 번호
	int y; // 상어 위치
	int x; // 상어 위치
	int head; // 상어가 어디를 바라보고 있는지

	// 우선순위
	// 0:위, 1:아래, 2:왼쪽, 3:오른쪽
	int d[4][4]; // 현재 상어가 보고 있는 방향, 우선순위
};

int n,m,k; // 격자 크기, 상어 개수, 냄새 남아있는 정도
int board[20][20]; // 보드 상어의 위치
pair<int,int> scent[20][20]; // 상어가 남긴 냄새 (상어번호, 남아있는 냄새)
vector<shark> s;
bool check[401]; // 상어 활성화 현황
int dy[4]={-1,1,0,0};
int dx[4]={0,0,-1,1};

void printBoard(){
	cout<<"---board---\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void printScent(){
	cout<<"---scent---\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<scent[i][j].first<<","<<scent[i][j].second<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>m>>k;

	// 상어 크기 미리 지정
	s.resize(401);

	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			int temp;
			cin>>temp;

			if(temp==0) {
				board[i][j]=0;
				continue;
			}

			// 상어일 경우 
			board[i][j]=temp;
			s[temp].idx=temp;
			s[temp].y=i;
			s[temp].x=j;
		}
	}

	// 상어가 바라보고 있는 방향
	for(int i=1;i<=m;i++){
		int direct;
		cin>>direct;
		s[i].head=direct-1;
	}

	// 각 상어의 우선순위
	for(int l=1;l<=m;l++){
		// 상어가 어디를 바라보고 있는지에 따라서
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				int x;
				cin>>x;
				s[l].d[i][j]=x-1;
			}
		}
	}

	// scent 설정
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			scent[i][j]={0,0};
		}
	}
}

bool OnlyOneShark(){
	for(int i=2;i<=m;i++){
		if(!check[i]) return false;
	}
	return true;
}

void remainScent(){
	for(int i=1;i<=m;i++){
		if(check[i]) continue;
		// 각 상어마다 현재 지금 있는 곳에 냄새를 남긴다.
		scent[s[i].y][s[i].x].first=s[i].idx;
		scent[s[i].y][s[i].x].second=k;
	}

}

// 냄새 하나씩 없어지는 것
void removeOneScent(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			// scent 칸에 냄새가 있다면 없앤다.
			// 만약 second가 0이라면 first도 초기화한다.
			if(scent[i][j].second==0) continue;

			scent[i][j].second--;

			if(scent[i][j].second==0) scent[i][j].first=0;

		}
	}

}

void move(){
	vector<pair<int,int>> tempBoard[20][20]; // 상어 인덱스, 보고있는 방향
	// cout<<"---print---\n";
	for(int i=1;i<=m;i++){
		if(check[i]) continue; // check true일 경우 비활성화된 상어
		int tempy=s[i].y;
		int tempx=s[i].x;

		bool sig=false;	
		// cout<<"*"<<i<<"\n";

		// 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
		for(int j=0;j<4;j++){

			int nextd=s[i].d[s[i].head][j];
			// cout<<tempy<<","<<tempx<<" * "<<nextd<<"\n";
			int ny=tempy+dy[nextd];
			int nx=tempx+dx[nextd];

			// 범위 벗어나면 안됨
			if(ny<0||nx<0||ny>=n||nx>=n) continue;

			// 냄새 남아있으면 안됨
			if(scent[ny][nx].second) continue;

			// 임시 보드에 상어 넣기 
			tempBoard[ny][nx].push_back({i,nextd}); // 상어 인덱스, 현재 바라보고 있는 방향
			sig=true;
			break;
		}

		// 못찾았을 경우, 자신의 냄새가 있는 칸의 방향으로 잡는다.
		if(!sig){
			for(int j=0;j<4;j++){
				int nextd=s[i].d[s[i].head][j];
				int ny=tempy+dy[nextd];
				int nx=tempx+dx[nextd];

				// 범위 벗어나면 안됨
				if(ny<0||nx<0||ny>=n||nx>=n) continue;

				// 내 냄새가 있어야함
				if(scent[ny][nx].first!=i) continue;

				// 임시 보드에 상어 넣기
				tempBoard[ny][nx].push_back({i,nextd});
				break;
			}
		}

		// cout<<"\n";
	}

	// for(int i=0;i<n;i++){
	// 	for(int j=0;j<n;j++){
	// 		cout<<i<<" "<<j<<": ";
	// 		for(auto e:tempBoard[i][j]){
	// 			cout<<e.first<<"&"<<e.second<<", ";
	// 		}
	// 		cout<<"\n";
	// 	}
	// }

	// 마지막에 같은 보드에 남아있는 경우, 처리
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(tempBoard[i][j].empty()){
				board[i][j]=0;
				continue;
			}else{
				// 갱신
				int sharkIdx=tempBoard[i][j][0].first;
				board[i][j]=sharkIdx;
				s[sharkIdx].head=tempBoard[i][j][0].second;
				s[sharkIdx].y=i;
				s[sharkIdx].x=j;
				for(int l=1;l<tempBoard[i][j].size();l++){
					check[tempBoard[i][j][l].first]=true;
				}	
			}
		}
	}

}

void solve(){

	for(int t=0;t<=1000;t++){
		// printBoard();
		// 1번 상어 제외 전부 check 배열이 true인 경우 
		if(OnlyOneShark()){
			cout<<t;
			return;
		}

		// 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
		remainScent();
		// printScent();

		// 이동한다. 
		move();

		// 냄새가 사라진다.
		removeOneScent();
	}

	cout<<"-1";


}

int main(){
	input();
	solve();
}