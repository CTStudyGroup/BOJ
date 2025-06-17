#include <iostream>

using namespace std;

int n;
int arr[500];
int ans=500;
void input(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		cin>>arr[i];
	}
}

int check(int s,int diff){
	int cnt=0;
	for (int i = 0; i < n; ++i)
	{
		if(arr[i]!=s) cnt++;
		s+=diff;
	}
	return cnt;
}

void solve(){
	for (int i = 0; i < n; ++i)
	{
		for (int j = i+1; j < n; ++j)
		{
			double diff=(arr[j]-arr[i])/(j-i);
			if(diff-(int)diff!=0) continue;
			int temp=check(arr[i]-diff*i,diff);
			if(ans>temp) ans=temp;
		}
	}
}

int main(){
	input();
	solve();
	cout<<ans;
}