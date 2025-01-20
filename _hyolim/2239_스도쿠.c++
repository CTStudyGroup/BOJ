#include <iostream>
#include <string>
#include <vector>
using namespace std;

int board[9][9]={0,};
struct point_t{
	int x;
	int y;
};
vector<point_t> vec;

void printBoard(){
	// cout<<"===========================\n";
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			cout<<board[i][j];
		}
		cout<<"\n";
	}
}

void printVec(){
	for(auto i:vec){
		cout<<i.x<<" "<<i.y<<"\n";
	}
	cout<<"\n";
}

void input(){
	for(int i=0;i<9;i++){
		string st;
		cin>>st;
		for(int j=0;j<9;j++){
			board[i][j]=st[j]-'0';
			if(!board[i][j]){
				point_t temp;
				temp.y=i;
				temp.x=j;
				vec.push_back(temp);
			}
		}
	}
}

void solve(int depth){
	if(depth==vec.size()){
		printBoard();
		exit(0);
	}
	// cout<<"Depth: "<<depth<<"\n";

	// 0에 들어갈 수 있는 숫자 구하기
	int arr[10]={0,};
	int y=vec[depth].y;
	int x=vec[depth].x;

	// 가로
	for(int i=0;i<9;i++){
		if(board[y][i]) {
			arr[board[y][i]]=1;
		}

	}

	// 세로
	for(int i=0;i<9;i++){
		if(board[i][x]) {
			arr[board[i][x]]=1;
		}
	}

	// 3*3
	int y3=y/3;
	// cout<<y3<<" "<<y3+3<<"\n";
	int x3=x/3;
	// cout<<x3<<" "<<x3+3<<"\n";

	for(int i=y3*3;i<y3*3+3;i++){
		for(int j=x3*3;j<x3*3+3;j++){
			if(board[i][j]) {
				// cout<<board[i][j];
				arr[board[i][j]]=1;
			}
		}
	}

	// cout<<"ARR : ";
	// for(int i=1;i<10;i++){
	// 	cout<<arr[i];
	// }


	// 재귀
	for(int i=1;i<10;i++){
		if(!arr[i]){
			// cout<<"B";
			// for(int i=1;i<10;i++){
			// 	cout<<arr[i];
			// }
			// cout<<"\n";
			board[y][x]=i;
			// printBoard();
			solve(depth+1);
			board[y][x]=0;
			// cout<<"A";
			// for(int i=1;i<10;i++){
			// 	cout<<arr[i];
			// }
			// cout<<"\n";
		}
	}
}

int main(){
	input();
	// printBoard();
	solve(0);
}