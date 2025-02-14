#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[100001]={0,};\
int summ=0;
int cnt2=0;
void input(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
		summ+=arr[i];
		cnt2+=arr[i]/2;
	}

}


void solve(){
	if(summ%3!=0) cout<<"NO";
	else{
		if(cnt2>=summ/3){
			cout<<"YES";
		}else{
			cout<<"NO";
		}
	}	
}

int main(){
	input();
	solve();
}