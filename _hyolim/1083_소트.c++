#include <iostream>

using namespace std;

int n,s;
int arr[50]={0,};

void input(){
	cin>>n;
	for (int i = 0; i < n; ++i)
	{
		cin>>arr[i];
	}
	cin>>s;	
}

void solve(){
	int st=0;
	while(st<n&&s>0){
		int maxidx=st;

		for (int i = st; i <= min(n-1,st+s); ++i)
		{
			if (arr[maxidx]<arr[i]) maxidx=i;
		}
		for(int i=maxidx;i>st;i--){
			swap(arr[i],arr[i-1]);
			s--;
		}
		st++;
	}
}

void output(){
	for (int i = 0; i < n; ++i)
	{
		cout<<arr[i]<<" ";
	}
}

int main(){
	input();
	solve();
	output();
}