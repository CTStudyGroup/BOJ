#include <iostream>
#include <vector>
using namespace std;

int n,m; // 노트북 세로, 가로 길이
int k; // 스티커 개수

int board[41][41]={0,};
int sticker[41][41]={0,};
int stN,stM;

void reset(){
	for(int i=0;i<41;i++){
		for(int j=0;j<41;j++){
			sticker[i][j]=0;
		}
	}
}

void input(){
	cin>>stN>>stM;
	for(int i=0;i<stN;i++){
		for(int j=0;j<stM;j++){
			cin>>sticker[i][j];
		}
	}
}

void printSticker(int _n,int _m){
	cout<<"============STICKER============\n";

	for(int i=0;i<_n;i++){
		for(int j=0;j<_m;j++){
			cout<<sticker[i][j];
		}
		cout<<"\n";
	}
}

void printBoard(){
	cout<<"============BOARD=============\n";

	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<board[i][j];
		}
		cout<<"\n";
	}
}


bool isFill(int y,int x){
	for(int i=0;i<stN;i++){
		for(int j=0;j<stM;j++){
			if(sticker[i][j]==0) continue;
			if(board[y+i][x+j]==sticker[i][j]) return false;
		}
	}
	return true;
}

void rot90(){
	int temp[41][41]={0,};
	for(int i=0;i<stN;i++){
		for(int j=0;j<stM;j++){
			temp[j][i]=sticker[stN-1-i][j];
		}	
	}

	int stTemp=stM;
	stM=stN;
	stN=stTemp;

	for(int i=0;i<stN;i++){
		for(int j=0;j<stM;j++){
			sticker[i][j]=temp[i][j];
		}
	}
	// printSticker(stN,stM);
}

void fillBoard(int y,int x){
	for(int i=0;i<stN;i++){
		for(int j=0;j<stM;j++){
			if(sticker[i][j]==0) continue;
			if(sticker[i][j]==1) board[y+i][x+j]=sticker[i][j];
		}
	}
}

void solve(){
	// printBoard();

	// 그대로 보드에 들어갈 수 있는지 확인
	// 보드 넘어가는지 확인
	// 돌리기~
	for(int r=0;r<4;r++){
		// cout<<"==============r==============\n";
		// cout<<n<<stN<<" "<<m<<stM<<"\n";
		// 위에서부터 쭉 들어갈 수 있는지 찾고, 넣기
		for(int i=0;i<=n-stN;i++){
			for(int j=0;j<=m-stM;j++){
				if(isFill(i,j)) {
					fillBoard(i,j);
					return;
				}
			}
		}
		// 없으면 스티커 돌리기
		rot90();
	}


}

void output(){
	int ans=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(board[i][j]==1) ans++;
		}
	}

	cout<<ans;
}

int main(){
	cin>>n>>m>>k;

	for(int i=0;i<k;i++){
		reset();
		input();
		solve();
		// printBoard();
	}

	output();

}