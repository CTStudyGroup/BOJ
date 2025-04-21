#include <iostream>
#include <vector>
#include <string>

using namespace std;

int t,k;
vector<vector<int>> wheel;
vector<int> wpoint;

void printWheel(){
	cout<<"---wheel--\n";
	for(int i=0;i<wheel.size();i++){
		cout<<i<<" : \n";
		for(auto e:wheel[i]){
			cout<<e;
		}
		cout<<"\n";
	}
}

void printWpoint(){
	cout<<"--p--\n";
	for(auto e:wpoint){
		cout<<e<<" ";
	}
	cout<<"\n";
}
void input(){
	cin>>t;
	for(int i=0;i<t;i++){
		string temp;
		cin>>temp;
		vector<int> tempv;
		for(auto e:temp){
			tempv.push_back(e-'0');
		}
		wheel.push_back(tempv);
		wpoint.push_back(0);
	}

	// printWheel();
}


void solve(int num,int d,bool r,bool l){ // r과 l은 오른쪽 왼쪽 움직여도 되는건지 확인용
	// cout<<"*"<<num<<" "<<d<<" "<<r<<" "<<l<<"\n";
	// 내 양 옆의 톱니바퀴를 회전시킬지 말지 고민해야함
	// 오른쪽 - 반대일 경우 반대로 돌리기
	if(num<t-1&&r){
		if(wheel[num][(wpoint[num]+2)%8] != wheel[num+1][(wpoint[num+1]+6)%8]){
			solve(num+1,-d,1,0); // 오른쪽으로 가는거는 오른쪽으로만 가도록
		}
	}

	// 왼쪽
	if(num>0&&l){
		if(wheel[num][(wpoint[num]+6)%8] != wheel[num-1][(wpoint[num-1]+2)%8]){
			solve(num-1,-d,0,1); // 왼쪽으로 가는거는 왼쪽으로만 가도록
		}
	}

	// 돌리기
	wpoint[num]=(wpoint[num]+d+8)%8;
	// printWpoint();
}

void output(){
	long answer=0;
	for(int i=0;i<t;i++){
		answer+=wheel[i][wpoint[i]];
	}
	cout<<answer;
}

int main(){
	input();
	cin>>k;
	while(k--){
		int num,d;
		cin>>num>>d;
		// cout<<"#";
		solve(num-1,-d,1,1);
	}
	// printWheel();
	output();

}

