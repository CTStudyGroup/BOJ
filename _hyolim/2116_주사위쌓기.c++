#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int dice[10001][6]={0,};
int dicebtm[6]={5,3,4,1,2,0};
long answer=0;

void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		for(int j=0;j<6;j++){
			cin>>dice[i][j];
		}
	}

	// for(int i=0;i<n;i++){
	// 	for(int j=0;j<6;j++){
	// 		cout<<dice[i][j]<<" ";
	// 	}
	// 	cout<<"\n";
	// }
}

// makeRec(?,1,?)
// 1번 주사위의  아랫면이 정해지면 나머지 쌓는 함수
void makeRec(int top,int idx,long sum){
	// 쌓을 때 가장 큰 숫자를 sum에 계속 넣기
	// 마지막에서 max 갱신하기
	if(idx==n){
		answer=max(sum,answer);
		return;
	}

	// 밑 주사위의 윗변이랑 같은 아랫면을 찾기
	for(int i=0;i<6;i++){
		if(top==dice[idx][i]){
			int maxnum=0;
			// top == i, bottom = dicebtm[i] 
			for(int j=0;j<6;j++){
				if(j==i || j==dicebtm[i]) continue;
				maxnum=max(maxnum,dice[idx][j]);
			}
			makeRec(dice[idx][dicebtm[i]],idx+1,sum+maxnum); // TODO:
		}
	}
}

void solve(){
	for(int i=0;i<6;i++){
		int maxnum=0;
		// top == i, bottom = dicebtm[i] 
		for(int j=0;j<6;j++){
			if(j==i || j==dicebtm[i]) continue;
			maxnum=max(maxnum,dice[0][j]);
		}
		makeRec(dice[0][dicebtm[i]],1,maxnum); // TODO:
		
	}

	cout<<answer;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
}