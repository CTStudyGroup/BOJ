#include <iostream>

using namespace std;

int c,p,answer;
int board[100];

void input(){
	cin>>c>>p;
	for(int i=0;i<c;i++){
		cin>>board[i];
	}
	answer=0;
}

void b1(){
	answer+=c;
	for(int i=0;i<c-3;i++){
		if(board[i]==board[i+1]&&board[i+1]==board[i+2]&&board[i+2]==board[i+3]) answer++;
	}
}

void b2(){
	for(int i=0;i<c-1;i++){
		if(board[i]==board[i+1]) answer++;
	}
}

void b3(){
	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]&&board[i+1]==board[i+2]-1) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]+1) answer++;

}

void b4(){
	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]+1&&board[i+1]==board[i+2]) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]-1) answer++;
}

void b5(){
	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]&&board[i+1]==board[i+2]) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]+1) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]-1) answer++;

	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]+1&&board[i+1]+1==board[i+2]) answer++;

}

void b6(){
	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]-1&&board[i+1]==board[i+2]) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]+2) answer++;

	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]&&board[i+1]==board[i+2]) answer++;

	
}
void b7(){
	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]&&board[i+1]==board[i+2]) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]) answer++;

	for(int i=0;i<c-1;i++)
		if(board[i]==board[i+1]-2) answer++;

	for(int i=0;i<c-2;i++)
		if(board[i]==board[i+1]&&board[i+1]==board[i+2]+1) answer++;

	
}

void solve(){
	if(p==1) b1();
	if(p==2) b2();
	if(p==3) b3();
	if(p==4) b4();
	if(p==5) b5();
	if(p==6) b6();
	if(p==7) b7();
	cout<<answer;
}

int main(){
	input();
	solve();
}