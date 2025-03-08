#include <iostream>

using namespace std;

int n;
int arr[1001];
int dp[1001]={0,};

int main(){
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>arr[i];
	}

	int max=0;
	for(int i=1;i<=n;i++){
		dp[i]=1;
		for(int j=1;j<i;j++){
			if(arr[j]<arr[i]&& dp[i]<dp[j]+1) dp[i]=dp[j]+1;
		}
		if(max<dp[i]) max=dp[i];
	}
	cout<<max;
}