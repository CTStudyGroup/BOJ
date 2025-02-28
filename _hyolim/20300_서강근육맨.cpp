#include <iostream>
#include <algorithm>

using namespace std;

long arr[10001];
int n;
long m=0;

int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}

	if(n==1){
		cout<<arr[0];
		exit(0);
	}
	sort(arr,arr+n);

	// 홀수면 가장 큰 수 빼기
	if(n%2==1) {
		m=arr[n-1];
		n=n-1;
	}
	for(int i=0;i<n/2;i++){
		if(m<arr[i]+arr[n-1-i]) m=arr[i]+arr[n-1-i];
	}
	cout<<m;
}