#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> vec;
int num[2000001]={0,};

void input(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		int temp; cin>>temp;
		vec.push_back(temp);
		num[temp]=1;
	}
}

void rec(int depth,int sum){
	num[sum]=true;
	if(depth==n) return;
	rec(depth+1,sum);
	rec(depth+1,sum+vec[depth]);

}

void solve(){
	rec(0,0);
}

void output(){

	for (int i = 1; i <= 2000000; ++i)
	{
		if (!num[i])
		{
			cout<<i;
			return;
		}
	}
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	input();
	solve();
	output();
}