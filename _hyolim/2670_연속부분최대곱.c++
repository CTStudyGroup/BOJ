#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main(){
	ios_base::sync_with_stdio(false);

	int n;
	cin>>n;
	vector<double> v;
	double dp[10001]={0.0,};
	double M=0.0;
	for(int i=0;i<n;i++){
		double num;
		cin>>num;
		v.push_back(num);
	}

		dp[0]=v[0];
		for(int i=0;i<n;i++){
			dp[i]=max(v[i],v[i]*dp[i-1]);
			M=max(M,dp[i]);
		}



		cout.precision(3);
		cout<<fixed<<M;
}