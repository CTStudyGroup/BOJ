#include <iostream>

using namespace std;

int n;

int main(){
	while(cin>>n){
		int ans=1;
		int k=1;

		while(true){
			if(ans%n==0) break;
			k++;
			ans=ans*10+1;
			ans%=n;
		}
		cout<<k<<"\n";
	}	
}