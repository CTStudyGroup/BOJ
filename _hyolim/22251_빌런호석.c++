#include <iostream>
#include <cmath>
#include <string>

using namespace std;

string n; // 총 몇 층까지 있는지
int k; // k자리 수
int p; // 최대 P개 반전
string x; // 실제 멈춘 층수

int num[10][7]={
{1,1,1,0,1,1,1},
{0,0,1,0,0,1,0},
{0,1,1,1,1,0,1},
{0,1,1,1,0,1,1},
{1,0,1,1,0,1,0},
{1,1,0,1,0,1,1},
{1,1,0,1,1,1,1},
{0,1,1,0,0,1,0},
{1,1,1,1,1,1,1},
{1,1,1,1,0,1,1}};

int cnum[10][10]={0,};
long answer=0;

void input(){
	cin>>n>>k>>p>>x;

	// 앞자리 비었을 경우 0 채워주기
	for(int i=x.length();i<k;i++){
		x='0'+x;
	}

	for(int i=n.length();i<k;i++){
		n='0'+n;
	}
}

int changecnt(int a, int b){
	int cnt=0;
	for(int i=0;i<7;i++){
		cnt+=abs(num[a][i]-num[b][i]);
	}
	return cnt;
}

bool checkzero(string str){
	for(int i=0;i<str.length();i++){
		if(str[i]!='0') return false;
	}
	return true;
}

void rec(string str,int depth,int cnt){ // 현재 숫자, 어느 자리 수를 보고있는지, 몇 번 LED 껐다가 켰는지
	if(depth==k){
		// 전부 다 0일 경우 안됨
		if(checkzero(str)) return;

		if(x==str) return;		
		if(n>=str){
			// cout<<str<<"\n";
			answer++;
		}
		return;
	}

	int remainp=p-cnt;
	int curnum=str[depth]-'0';

	for(int i=0;i<10;i++){
		if(remainp-cnum[curnum][i]<0) continue; 
		str[depth]=((char)('0'+i));
		rec(str,depth+1,cnt+cnum[curnum][i]);
	}
}

void solve(){
	// 각 숫자마다 바뀌려면 얼마나 바뀌어야하는지 - cnum 채우기
	for(int i=0;i<10;i++){
		for(int j=0;j<10;j++){
			if(i==j) continue;
			cnum[i][j]=changecnt(i,j);
		}
	}

	// 각 숫자를 p개 이하 반전해서 얻을 수 있는 수 찾기
	rec(x,0,0);

}

int main(){
	input();
	solve();
	cout<<answer;
}