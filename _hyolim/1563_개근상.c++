#include <iostream>

using namespace std;

// 0 : 출석, 1 : 지각, 2 : 결석
int n;
long cnt=0;

void solve(int depth,int late,int absence){
	if(late>=2) return; // 지각 두 번 이상
	if(absence>=3) return; // 결석 3번 연속

	if(depth==n){
		cnt=(cnt+1)%1000000;
		return;
	}


	solve(depth+1,late,0); //출석
	solve(depth+1,late,absence+1); //결석
	solve(depth+1,late+1,0); //지각
}

int main(){
	cin>>n;
	solve(0,0,0);
	cout<<cnt;

}