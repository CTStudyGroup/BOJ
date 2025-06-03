#include <iostream>
using namespace std;

long long int dp[1000001][2];

long long int cal_dp(int x){
  for(int i =3; i<=x; i++){
    dp[i][1] = (dp[i-3][0] +dp[i-1][1])%1000000007;
    dp[i][0] = (3*dp[i-2][0]+2*dp[i-1][0]+2*dp[i][1])%1000000007;
  }
  return dp[x][0];
}

int main() {
 dp[0][0] = 0;
 dp[1][0] = 2;
 dp[2][0] = 7;
 dp[2][1] = 1;
 int n;
 cin >> n;
 cout << cal_dp(n);
}