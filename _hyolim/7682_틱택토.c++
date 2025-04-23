#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> x; // x의 위치
vector<int> o; // o의 위치
vector<bool> xv; // x용 visited
vector<bool> ov; // o용 visited
bool sig=false;

void reset(){
	x.clear();
	o.clear();
	xv.clear();
	ov.clear();
	sig=false;
}

void printXO(){
	cout<<"---xo---\n";
	for(auto e:x){
		cout<<e<<" ";
	}
	cout<<"\n";

	for(auto e:o){
		cout<<e<<" ";
	}
	cout<<"\n";
}

void input(string temp){
	for(int i=0;i<9;i++){
		if(temp[i]=='X') x.push_back(i);
		if(temp[i]=='O') o.push_back(i);
	}

	for(auto e:x){
		xv.push_back(false);
	}
	for(auto e:o){
		ov.push_back(false);
	}

	// printXO();
}

// 보드에서 승자가 나왔는지
bool checkF(vector<int> board){
	// 가로 확인
	if(board[0]==board[1]&&board[1]==board[2]&&board[2]!=-1) return true;
	if(board[3]==board[4]&&board[4]==board[5]&&board[5]!=-1) return true;
	if(board[6]==board[7]&&board[7]==board[8]&&board[8]!=-1) return true;

	// 세로 확인
	if(board[0]==board[3]&&board[3]==board[6]&&board[6]!=-1) return true;
	if(board[1]==board[4]&&board[4]==board[7]&&board[7]!=-1) return true;
	if(board[2]==board[5]&&board[5]==board[8]&&board[8]!=-1) return true;

	// 대각선 확인
	if(board[0]==board[4]&&board[4]==board[8]&&board[8]!=-1) return true;
	if(board[2]==board[4]&&board[4]==board[6]&&board[6]!=-1) return true;

	return false;
}	

// 최종상태인지 확인하는 코드
bool checkXO(vector<int> xtemp,vector<int> otemp){
	vector<int> board;
	for(int i=0;i<9;i++){
		board.push_back(-1);
	}
	// cout<<"#";
	// 번갈아가면서 채우기
	while(!xtemp.empty()||!otemp.empty()){
		if(!xtemp.empty()){ // 비어있지 않으면 하나 출력
			board[xtemp[xtemp.size()-1]]=0;
			xtemp.pop_back();
			if(checkF(board)){
				if(xtemp.empty()&&otemp.empty()) return true; // 만약 다 넣었을 경우

				return false;
			}
		}
		if(!otemp.empty()){ // 비어있지 않으면 하나 출력
			board[otemp[otemp.size()-1]]=1;
			otemp.pop_back();
			if(checkF(board)){
				if(xtemp.empty()&&otemp.empty()) return true; // 만약 다 넣었을 경우

				return false; //다 안넣었는데 승자가 나오면 False
			}
		}
	}

	for(int i=0;i<9;i++){
		if(board[i]==-1) return false;
	}

	return true;

}

void makeO(int depth,vector<int> xtemp,vector<int> otemp){
	if(sig) return;
	if(depth==o.size()){
		if(checkXO(xtemp,otemp)){ // 최종 상태일 경우
			cout<<"valid\n";
			sig=true;
		}
		return;
	}

	for(int i=0;i<o.size();i++){
		if(ov[i]) continue;
		ov[i]=true;
		otemp.push_back(o[i]);
		makeO(depth+1,xtemp,otemp);
		otemp.pop_back();
		ov[i]=false;
	}
}

void makeX(int depth,vector<int> xtemp){
	if(sig) return;
	if(depth==x.size()){
		vector<int> t;
		makeO(0,xtemp,t);
		return;
	}

	for(int i=0;i<x.size();i++){
		if(xv[i]) continue;
		xv[i]=true;
		xtemp.push_back(x[i]);
		makeX(depth+1,xtemp);
		xtemp.pop_back();
		xv[i]=false;
	}
}

void solve(){
	// x,o 개수 검증, x가 o보다 1 많거나, x와 o의 개수가 같아야한다.
	if(x.size()!=o.size()+1&&x.size()!=o.size()){
		cout<<"invalid\n";
		return;
	}

	// x,o 조합을 만들어서 되는지 확인하기
	vector<int> t;
	makeX(0,t);
	if(!sig) cout<<"invalid\n";
}

int main(){
	string temp;
	cin>>temp;
	while(temp!="end"){
		reset();
		input(temp);
		solve();
		cin>>temp;
	}
}