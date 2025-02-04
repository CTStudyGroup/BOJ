#include <iostream>

using namespace std;

int n;
int board[21][21]={0,};
int visited[21][21]={0,};

int ans=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cin>>board[i][j];
		}
	}
}

void printB(){
	cout<<"-----------------------------\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void setV(){
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			visited[i][j]=0;
		}
	}
}
void moveUp(){
    setV();
    // 합치기
    for(int j=0;j<n;j++){
        for(int i=1;i<n;i++){ // 위에서 아래 방향으로 진행
            if(board[i][j] == 0) continue;
            for(int k=i-1;k>=0;k--){
                if(board[k][j] == 0) continue;
                if(board[k][j] == board[i][j] && !visited[k][j]){
                    board[k][j] *= 2;
                    board[i][j] = 0;
                    visited[k][j] = 1; // 이미 합쳐진 블록 표시
                }
                break;
            }
        }
    }
    // 옮기기
    for(int j=0;j<n;j++){
        for(int i=1;i<n;i++){
            if(board[i][j] == 0) continue;
            int k = i;
            while(k-1 >= 0 && board[k-1][j] == 0){
                board[k-1][j] = board[k][j];
                board[k][j] = 0;
                k--;
            }
        }
    }
}

void moveDown(){
    setV();
    // 합치기
    for(int j=0;j<n;j++){
        for(int i=n-2;i>=0;i--){ // 아래에서 위로 진행
            if(board[i][j] == 0) continue;
            for(int k=i+1;k<n;k++){
                if(board[k][j] == 0) continue;
                if(board[k][j] == board[i][j] && !visited[k][j]){
                    board[k][j] *= 2;
                    board[i][j] = 0;
                    visited[k][j] = 1; // 이미 합쳐진 블록 표시
                }
                break;
            }
        }
    }
    // 옮기기
    for(int j=0;j<n;j++){
        for(int i=n-2;i>=0;i--){
            if(board[i][j] == 0) continue;
            int k = i;
            while(k+1 < n && board[k+1][j] == 0){
                board[k+1][j] = board[k][j];
                board[k][j] = 0;
                k++;
            }
        }
    }
}

void moveRight(){
    setV();
    // 합치기
    for(int j=0;j<n;j++){
        for(int i=n-2;i>=0;i--){ // 오른쪽에서 왼쪽으로 진행
            if(board[j][i] == 0) continue;
            for(int k=i+1;k<n;k++){
                if(board[j][k] == 0) continue;
                if(board[j][k] == board[j][i] && !visited[j][k]){
                    board[j][k] *= 2;
                    board[j][i] = 0;
                    visited[j][k] = 1; // 이미 합쳐진 블록 표시
                }
                break;
            }
        }
    }
    // 옮기기
    for(int j=0;j<n;j++){
        for(int i=n-2;i>=0;i--){
            if(board[j][i] == 0) continue;
            int k = i;
            while(k+1 < n && board[j][k+1] == 0){
                board[j][k+1] = board[j][k];
                board[j][k] = 0;
                k++;
            }
        }
    }
}

void moveLeft(){
    setV();
    // 합치기
    for(int j=0;j<n;j++){
        for(int i=1;i<n;i++){ // 왼쪽에서 오른쪽으로 진행
            if(board[j][i] == 0) continue;
            for(int k=i-1;k>=0;k--){
                if(board[j][k] == 0) continue;
                if(board[j][k] == board[j][i] && !visited[j][k]){
                    board[j][k] *= 2;
                    board[j][i] = 0;
                    visited[j][k] = 1; // 이미 합쳐진 블록 표시
                }
                break;
            }
        }
    }
    // 옮기기
    for(int j=0;j<n;j++){
        for(int i=1;i<n;i++){
            if(board[j][i] == 0) continue;
            int k = i;
            while(k-1 >= 0 && board[j][k-1] == 0){
                board[j][k-1] = board[j][k];
                board[j][k] = 0;
                k--;
            }
        }
    }
}

int findMax(){
	int mm=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(mm<board[i][j]) mm=board[i][j];
		}
	}
	return mm;
}


void solve(int depth){
	if(depth==5){
		int m=findMax();
		if(ans<m) ans=m;
		return;
	}
	int tempB[21][21]={0,};
	for(int i=0;i<4;i++){
		for(int x=0;x<n;x++){
			for(int y=0;y<n;y++){
				tempB[x][y]=board[x][y];
			}
		}
		if(i==0) moveUp(); 
		if(i==1) moveDown();
		if(i==2) moveRight();
		if(i==3) moveLeft();
		// printB();
		solve(depth+1);
		for(int x=0;x<n;x++){
			for(int y=0;y<n;y++){
				board[x][y]=tempB[x][y];
			}
		}
	}
}

void output(){
	cout<<ans;
}


int main(){
	input();
	solve(0);
	output();
}