#include <iostream>

using namespace std;

int t;
int n;
long dp[100002][2]={0,};
long dp2[100002]={0,};
// DP 테이블 정의 : 각 원소에 해당하는 수에서 가능한 방법의 수
// n에 대해서 알고싶다면, n/2에 해당하는 수를 더했을 때 n이 되는지 확인
// 이때, 가운데에 1,2,3이 들어갈 수도 있음 그래도 되는지 확인 -> 짝수의 경우에만 가능
// 홀수 일때는 가운데에 뭐가 들어가면 안됨 -> 홀수인거 저장하기
// 0: 전체 개수, 1:짝수 개수

int main(){
	dp2[1]=1;
	dp2[2]=2;
	dp2[3]=4;

	for(int i=4;i<=100000;i++){
		dp2[i]=(dp2[i-1]+dp2[i-2]+dp2[i-3])%1000000009;
	}

	dp[1][0]=1;

	dp[2][0]=2;
	dp[2][1]=1;

	dp[3][0]=2;

	for(int i=4;i<=100000;i++){
		// 중간에 아무것도 안넣었을 때 2로 나눠떨어지는 경우
		if(i%2==0) {
			dp[i][0]+=dp2[i/2]%1000000009;
			dp[i][1]+=dp2[i/2]%1000000009;
		}

		// 1넣었을 때 2로 나눠떨어지는 경우
		if((i-1)%2==0) dp[i][0]+=dp[i-1][1]%1000000009;

		// 2넣었을 때 2로 나눠떨어지는 경우
		if((i-2)%2==0) dp[i][0]+=dp[i-2][1]%1000000009;

		// 3넣었을 때 2로 나눠떨어지는 경우
		if((i-3)%2==0) dp[i][0]+=dp[i-3][1]%1000000009;
	}
	// for(int i=1;i<=10;i++){
	// 	cout<<i<<": "<< dp[i][0]<<" "<<dp[i][1]<<"\n";
	// }

	cin>>t;
	while(t--){
		cin>>n;
		cout<<dp[n][0]%1000000009<<"\n";
	}

}