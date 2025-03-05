#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// 각 번호에 따라서 재귀를 다양하게 들어감
int n,m;
vector<vector<int>> board;

int minsum=987654321;
struct point_t{
	int y;
	int x;
};

vector<point_t> cctv;
vector<vector<int>> tempb;
int first[4][4]={{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1}};
int second[2][4]={{1,1,0,0},{0,0,1,1}};
int third[4][4]={{1,0,0,1},{0,1,0,1},{0,1,1,0},{1,0,1,0}};
int fourth[4][4]={{1,1,1,0},{1,1,0,1},{1,0,1,1},{0,1,1,1}};
int fifth[4]={1,1,1,1};

void printB(){
	cout<<"-----------------------------\n";
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cout<<board[i][j]<<" ";
		}
		cout<<"\n";
	}
}

void input(){
	cin>>n>>m;
    board.assign(n, vector<int>(m));
    tempb.assign(n,vector<int>(m));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> board[i][j];
            tempb[i][j]=board[i][j];
            if(board[i][j] >= 1 && board[i][j] <= 5){
                cctv.push_back({i, j});
            }
        }
    }

}

void printvb(vector<vector<int>> temp){
	cout<<"------------\n";
	for(auto e:temp){
		for(auto w:e){
			cout<<w<<" ";
		}
		cout<<"\n";
	}
}


// 뻗어나가는거 // 상하좌우 
vector<vector<int>> spread(bool up,bool down,bool right,bool left,int y,int x,vector<vector<int>> temp){
	if(up){
		for(int i=y-1;i>=0;i--) {
			if(board[i][x]==6) break;
			if(board[i][x]) continue;
			temp[i][x]=-1;
		}
	}

	if(down){
		for(int i=y+1;i<n;i++) {
			if(board[i][x]==6) break;
			if(board[i][x]) continue;
			temp[i][x]=-1;
		}
	}
	
	if(right){
		for(int i=x+1;i<m;i++) {
			if(board[y][i]==6) break;
			if(board[y][i]) continue;
			temp[y][i]=-1;
		}
	}

	if(left){
		for(int i=x-1;i>=0;i--) {
			if(board[y][i]==6) break;
			if(board[y][i]) continue;
			temp[y][i]=-1;
		}
	}

	return temp;
}

int check(vector<vector<int>> temp){
	int cnt=0;
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(temp[i][j]==0) cnt++;
		}
	}
	return cnt;
}

void solve(int idx,vector<vector<int>> temp){
	if(idx>=cctv.size()){
		// printvb(temp);
		minsum=min(minsum,check(temp));

		return;
	}
	vector<vector<int>> temp2;

	int y=cctv[idx].y;
	int x=cctv[idx].x;
	int num=board[y][x];

	if(num==1){
		for(int i=0;i<4;i++){
			temp2=spread(first[i][0],first[i][1],first[i][2],first[i][3],y,x,temp);
			solve(idx+1,temp2);
		}
	}

	if(num==2){
		for(int i=0;i<2;i++){
			temp2=spread(second[i][0],second[i][1],second[i][2],second[i][3],y,x,temp);
			solve(idx+1,temp2);
		}
	}

	if(num==3){
		for(int i=0;i<4;i++){
			temp2=spread(third[i][0],third[i][1],third[i][2],third[i][3],y,x,temp);
			solve(idx+1,temp2);
		}
	}

	if(num==4){
		for(int i=0;i<4;i++){
			temp2=spread(fourth[i][0],fourth[i][1],fourth[i][2],fourth[i][3],y,x,temp);
			solve(idx+1,temp2);
		}
	}

	if(num==5){
		temp2=spread(fifth[0],fifth[1],fifth[2],fifth[3],y,x,temp);
		solve(idx+1,temp2);
	}

	
}

int main(){
	input();
	solve(0,tempb);
	cout<<minsum;
}