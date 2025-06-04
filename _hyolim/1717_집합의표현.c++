#include <iostream>

using namespace std;

int n,m;
int arr[1000010]={0,};



void funca(int a,int b){
	if(a<=b){
		arr[b]=arr[a];
	}else{
		arr[a]=arr[b];
	}
}

void funcb(int a,int b){
	if(arr[a]==arr[b]) cout<<"YES\n";
	else cout<<"NO\n";

}

int main(){
	cin>>n>>m;
	for (int i = 0; i <= n; ++i)
	{
		arr[i]=i;
	}

	for (int i = 0; i < m; ++i)
	{
		int t,a,b; cin>>t>>a>>b;
		if (t==0)
		{
			funca(a,b);
		}else{
			funcb(a,b);
		}
	}
}