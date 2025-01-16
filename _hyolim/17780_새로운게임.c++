#include <iostream>
#include <vector>

using namespace std;
// 1base

struct point_t{
	int p; // 말 번호
	int w; // 어디로 갈건지
	int y; // 행
	int x; // 열
};

int direct[5][2]={{0,0},{0,1},{0,-1},{-1,0},{1,0}}; // 오른쪽, 왼쪽, 위, 아래
int n,k; // 체스판의 크기, 말의 개수
int board[13][13]={0,}; // 체스판 0흰색, 1빨간색, 2파란색
vector<point_t> vec[11]; // 2차원 연결리스트, 인덱스가 바닥번호, 위로 하나씩 쌓임
int cnt=1;

/*
	흰색 : 그냥 이동 + 누가 있으면 위에 얹기
	빨간색 : 이동 + (움직인 애만) 순서 뒤엎기
	파란색  : 이동방향 반대로 바꿈 + 한칸 이동
*/

// 말이 4개 이상 쌓이는 순간 게임 종료
// 게임이 종료되는 턴의 번호 출력, 턴의 번호가 1000보다 클 경우 종료

void printBoard(){
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cout<<board[i][j];
		}
		cout<<"\n";
	}
}

void printVec(){
	cout<<"\n========VEC========\n";
	for(int i=1;i<=k;i++){
		for(int j=0;j<vec[i].size();j++){
			cout<<vec[i][j].p<<" "<<vec[i][j].w<<" 좌표 : "<<vec[i][j].y<<" "<<vec[i][j].x<<" , ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>k;

	// 보드 정보 받기
	for(int i=1;i<=n;i++){
		for(int j=1;j<=n;j++){
			cin>>board[i][j];
		}
	}

	// 말 정보 받기
	for(int i=1;i<=k;i++){
		int y,x,w; // 행,열,방향
		cin>>y>>x>>w;
		point_t temp = {i,w,y,x};
		vec[i].push_back(temp);
	}
}

bool isStack4(){
	for(int i=1;i<=k;i++){
		if(vec[i].size()>=4){
			return true;
		}
	}
	return false;
}

bool isGo(int _y,int _x){
	if(_y<=0) return false;
	if(_x<=0) return false;
	if(_y>n) return false;
	if(_x>n) return false;
	return true;
}

void move(int idx,int _y,int _x){ // 어느 말에 해당되는 애가 어디로 움직일건지
	for(int i=0;i<vec[idx].size();i++){
		vec[idx][i].y=_y;
		vec[idx][i].x=_x;
	}

}

int findP(int _y,int _x){
	for(int i=1;i<=k;i++){
		if(vec[i].size()>0){
			if(vec[i][0].y==_y && vec[i][0].x==_x){
				return i;
			}
		}
	}
	return -1;
}

void solve(){
	while(cnt<=1000){
		// 모든 말 각각 옮겨보기, vec[n][0]이 아닐 경우 못움직임
		for(int i=1;i<=10;i++){

			if(vec[i].size()>0){
				// vec[i][0] = 얘가 맨 밑에 있는 애
				// 얘가 원하는 방향으로 갔을 때 어느 색의 칸인지 보기
				int nextY=vec[i][0].y+direct[vec[i][0].w][0];
				int nextX=vec[i][0].x+direct[vec[i][0].w][1];

				// nextY, nextX 범위 체크
				// 파란색이거나 체스판 벗어났을 때
				if(board[nextY][nextX]==2 || !isGo(nextY,nextX)){ 
					// 이동방향 바꾸기
					if(vec[i][0].w==1){ // 오른쪽, 2로 바꿔야함
						vec[i][0].w=2;
					}
					else if(vec[i][0].w==2){ // 왼쪽, 1로 바꿔야함
						vec[i][0].w=1;
					}
					else if(vec[i][0].w==3){ // 위쪽, 4로 바꿔야함
						vec[i][0].w=4;
					}
					else if(vec[i][0].w==4){ // 아래쪽, 3로 바꿔야함
						vec[i][0].w=3;					
					}

					// 다시 갈 곳을 보기
					nextY=vec[i][0].y+direct[vec[i][0].w][0];
					nextX=vec[i][0].x+direct[vec[i][0].w][1];
				}

				// cout<<i<<" "<<nextY<<" "<<nextX<<"\n";
				// 흰색
				if(board[nextY][nextX]==0){
					// cout<<"white";
					if(isGo(nextY,nextX)){
						// 이동하려는 칸에 말이 이미 있는 경우 뒤에 넣기
						// nextY,nextX를 점유하고 있는 vec[i] 찾기
						int idx=findP(nextY,nextX);
						move(i,nextY,nextX);

						if(idx!=-1){ // 이미 그 칸을 점령하고 있는 애가 있다.
							for(int j=0;j<vec[i].size();j++){
								// 뒤에 넣기
								vec[idx].push_back(vec[i][j]);
							}
							vec[i].clear();
						} 	

					}
				}

				// 빨간색
				if(board[nextY][nextX]==1){
					// cout<<"red";
					int tempIdx=0;
					if(isGo(nextY,nextX)){
						// 이동하려는 칸에 말이 이미 있는 경우 뒤에 넣기
						// nextY,nextX를 점유하고 있는 vec[i] 찾기
						int idx=findP(nextY,nextX);
						move(i,nextY,nextX);

						if(idx!=-1){ // 이미 그 칸을 점령하고 있는 애가 있다.
							for(int j=vec[i].size()-1;j>=0;j--){
								// 순서 바꿔서 넣기
								vec[idx].push_back(vec[i][j]);
							}
							vec[i].clear();
						}
						else{ 
							// 없다면 순서만 바꾸기
							tempIdx=vec[i][vec[i].size()-1].p;
							if(i!=tempIdx){
								// 맨 뒤에서부터 넣기 
								for(int j=vec[i].size()-1;j>=0;j--){
									vec[tempIdx].push_back(vec[i][j]);
								}
								vec[i].clear();

							}
							
						}
					}
				}

				// 스택 4개 이상 쌓였을 경우 종료
				if(isStack4()) return;
			}
		}
		// printVec();

		cnt++;
		// cout<<"cnt : "<<cnt<<" \n";
	}

}

void output(){
	if(cnt>1000) cout<<"-1";
	else cout<<cnt;
}

int main(){
	input();
	// printVec();
	solve();
	output();
}