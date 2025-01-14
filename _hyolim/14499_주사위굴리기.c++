#include <iostream>

using namespace std;

// 각 인덱스별로 어디로 움직이는지에 대한 배열
// 1번이 맨 위에 있는 수 -> 출력
// 6번으로 보드랑 다이스 업데이트
// 나머지는 이동만
int r[7]={0,3,2,6,1,5,4};
int l[7]={0,4,2,1,6,5,3};
int d[7]={0,2,6,3,4,1,5};
int u[7]={0,5,1,3,4,6,2};
int dice[7]={0,0,0,0,0,0,0}; // 1-base
int n,m;
int x,y;
int k;
int board[21][21]={0,};

void input(){
	cin>>n>>m>>x>>y>>k;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>board[i][j];
		}
	}

} 

void changeBoard(){
	// 보드 변경
	if(board[x][y]==0){
		board[x][y]=dice[6];
	}else{
		dice[6]=board[x][y];
		board[x][y]=0;
	}
	cout<<dice[1]<<"\n";
}

bool isGo(int _p){
	if(_p==1 && y>=m-1){
		return false;
	}
	if(_p==2 && y<=0){
		return false;
	}
	if(_p==3 && x<=0){
		return false;
	}
	if(_p==4 && x>=n-1){
		return false;
	}
	return true;
}

void printDice(){
	cout<<"dice====\n";
	for(int i=1;i<=6;i++){
		cout<<dice[i]<<" ";
	}
	cout<<"========\n";
}
void east(){
	int new_dice[7]={0,};
	for(int i=1;i<=6;i++){
		new_dice[r[i]]=dice[i];
	}
	// 복사
	for(int i=1;i<=6;i++){
		dice[i]=new_dice[i];
	}
}

void west(){
	int new_dice[7]={0,};
	for(int i=1;i<=6;i++){
		new_dice[l[i]]=dice[i];
	}
	// 복사
	for(int i=1;i<=6;i++){
		dice[i]=new_dice[i];
	}
}

void south(){
	int new_dice[7]={0,};
	for(int i=1;i<=6;i++){
		new_dice[d[i]]=dice[i];
	}
	// 복사
	for(int i=1;i<=6;i++){
		dice[i]=new_dice[i];
	}
}

void north(){
	int new_dice[7]={0,};
	for(int i=1;i<=6;i++){
		new_dice[u[i]]=dice[i];
	}
	// 복사
	for(int i=1;i<=6;i++){
		dice[i]=new_dice[i];
	}
}

void solve(){
	// 동서남북 받기
	int p;

	// 명령어 횟수만큼 반복
	for(int ki=0;ki<k;ki++){
		cin>>p;
		// cout<<"p : "<<p<<"\n";
		if(!isGo(p)) continue; // 갈 수 없으면 무시
		// 주사위 변경
		if(p==1){
			east();
			y++;
		}else if(p==2){
			y--;
			west();
		}else if(p==3){
			x--;
			north();
		}else if(p==4){
			x++;
			south();
		}
		// printDice();
		// 보드 변경
		// cout<<"X : "<<x<<" y : "<<y<<"\n";
		changeBoard();
	}
}

void print_board(){
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void output(){

}

int main(){
	input();
	// print_board();
	solve();
	output();
}                