#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int n;
long dp[110]={0,};

void hanoi(int depth,int start,int bypass,int end){
	if(depth==1){
		cout<<start<<" "<<end<<"\n";
		return;
	}
	hanoi(depth-1,start,end,bypass); // 큰 원판 제외, depth-1개의 원판을 start->bypass로 옮긴다.
	cout<<start<<" "<<end<<"\n"; // 가장 큰 원판을 start->end로 직접 옮긴다.
	hanoi(depth-1,bypass,start,end); // 작은 원판들을 bypass에 있는 depth-1개의 원판을 end로 옮긴다.
}

void solve(){
	// dp 테이블 채우기
	string a=to_string(pow(2,n));

	int x = a.find('.');
	a = a.substr(0, x);
	a[a.length() - 1] -= 1;	
	cout<<a<<"\n";

	// 과정 출력하기
	if(n<=20) hanoi(n,1,2,3);
}

int main(){
	cin>>n;
	solve();
}