#include <iostream>
#include <algorithm>
using namespace std;

int n;
int total=0;
int cnt=0;
int arr[101];
void input(){
	cin>>n;

	for(int i=0;i<n;i++){
		cin>>arr[i];
		total+=arr[i];
	}
	sort(arr,arr+100,greater<int> ());
}

void solve(){
	while(cnt<=1440){

		if(total==0){
			cout<<cnt;
			return;
		}
		sort(arr,arr+100,greater<int> ());
	
		for(int i=0;i<n;i++){
			if(!arr[i]) continue;
			cnt++;
			total--;
			arr[i]--;
			for(int j=i+1;j<n;j++){
				if(!arr[j]) continue;
				total--;
				arr[j]--;
				// cout<<i<<" "<<j<<" "<<cnt<<" "<<total<<"\n";
				break;
			}
			break;
		}
	}
	cout<<"-1";
}

int main(){
	input();
	solve();
}