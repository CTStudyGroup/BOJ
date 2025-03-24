#include <iostream>

using namespace std;

// 구간합 문제
// s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+arr[i][j];

int r,c,q;
long arr[1001][1001]={0,};
long s[1001][1001]={0,};

int main(){
	cin>>r>>c>>q;

	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++){
			cin>>arr[i][j];
		}
	}

	// 구간합 배열 채우기
	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++){
			s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+arr[i][j];
		}
	}

	// q만큼 대답하기
	while(q--){
		int r1,c1,r2,c2;
		cin>>r1>>c1>>r2>>c2;
		int summ=(s[r2][c2]-s[r1-1][c2]-s[r2][c1-1]+s[r1-1][c1-1]);
		int cnt=(r2-r1+1 )*(c2-c1+1);
		cout<<summ/cnt<<"\n";
	}
}