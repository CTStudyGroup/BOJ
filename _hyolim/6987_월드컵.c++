#include <iostream>
#define FOR(i,st,en) for(int i=st;i<en;++i)
using namespace std;

int arr[6][3];

void input(){
	FOR(i,0,6)
		FOR(j,0,3)
			cin>>arr[i][j];

}

bool solve(){
	// 행마다 다 합쳤을 때 5판 나오는지 확인
	FOR(i,0,6){
		int summ=0;
		FOR(j,0,3){
			summ+=arr[i][j];
		}
		if(summ!=5){
			return false;
		}
	}

	// 각 승리가 다른 나라에게 잘 분배되었는지 확인
	FOR(i,0,6){
		FOR(j,1,6){
			int ti=(j+i)%6;
			// cout<<i<<" "<<ti<<"\n";
			// 승리가 0이되면 계산 끝
			if(arr[i][0]==0) break;
			if(arr[ti][2]){ // 뭐가 있으면 1씩 차감
				arr[i][0]--;
				arr[ti][2]--; 
			}
		}
		// 만약 다 정리했는데 승리가 남아있다면?
		if(arr[i][0]) return false;
	}
	// 다 정리했는데 패배가 남아있다면?
	FOR(i,0,6){
		if(arr[i][2]) return false;
	}

	// 무승부
	int temp=0;
	FOR(i,0,6){
		temp=abs(temp-arr[i][1]);
	}
	if(temp!=0) return false;	

	return true;
}

int main(){
	FOR(i,0,4){
		input();
		cout<<solve()<<" ";
	}
}
